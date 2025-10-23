# swallow_model.py
from typing import Optional, Tuple, List, Any, Union
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor

from transformers import (
    GemmaPreTrainedModel,
    GemmaModel,
)
from transformers.modeling_outputs import CausalLMOutputWithPast


class SwallowForCausalLM(GemmaPreTrainedModel):
    """
    Gemma を内包した CausalLM ラッパー。
    - from_pretrained() で Gemma の学習済み重みを読める
    - generate() / use_cache / beam_search に対応
    - weight tying（embed_tokens と lm_head）を実施
    """

    def __init__(self, config):
        super().__init__(config)
        self.model = GemmaModel(config)
        # 出力ヘッド（weight tying するので bias=False）
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)
        self.post_init()  # HFの標準初期化フック

    # ---- Embedding / Head の getter/setter（weight tying 用） ----
    def get_input_embeddings(self) -> nn.Embedding:
        return self.model.embed_tokens

    def set_input_embeddings(self, new_emb: nn.Embedding):
        self.model.embed_tokens = new_emb

    def get_output_embeddings(self) -> nn.Linear:
        return self.lm_head

    def set_output_embeddings(self, new_out: nn.Linear):
        self.lm_head = new_out

    def tie_weights(self):
        # 入力埋め込みと lm_head を結合（重み共有）
        if self.get_output_embeddings() is not None and self.get_input_embeddings() is not None:
            self._tie_or_clone_weights(self.lm_head, self.get_input_embeddings())

    # ---- forward：CausalLM 互換の出力を返す ----
    def forward(
        self,
        input_ids: Optional[Tensor] = None,
        attention_mask: Optional[Tensor] = None,
        position_ids: Optional[Tensor] = None,
        past_key_values: Optional[Tuple[Tuple[Tensor]]] = None,
        inputs_embeds: Optional[Tensor] = None,
        use_cache: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        labels: Optional[Tensor] = None,
        return_dict: Optional[bool] = True,
        **kwargs,
    ) -> Union[CausalLMOutputWithPast, Tuple[Tensor, ...]]:

        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=True,
            **kwargs,
        )

        hidden_states = outputs.last_hidden_state  # [B, T, H]
        logits = self.lm_head(hidden_states)       # [B, T, V]

        loss = None
        if labels is not None:
            # GPT系の言語モデリング損失（次トークン予測）
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            loss = F.cross_entropy(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1), ignore_index=-100)

        if not return_dict:
            output = (logits, outputs.past_key_values, outputs.hidden_states, outputs.attentions)
            return ((loss,) + output) if loss is not None else output

        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=outputs.past_key_values,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

    # ---- generate() 用の入力整形（KVキャッシュ使用時に末尾トークンだけ渡す）----
    def prepare_inputs_for_generation(
        self,
        input_ids: Tensor,
        past_key_values: Optional[Tuple[Tuple[Tensor]]] = None,
        attention_mask: Optional[Tensor] = None,
        inputs_embeds: Optional[Tensor] = None,
        **kwargs,
    ):
        if past_key_values is not None:
            # 直近トークンのみ供給（高速化）
            input_ids = input_ids[:, -1:]
            if attention_mask is not None:
                attention_mask = attention_mask[:, -1:]

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "past_key_values": past_key_values,
            "use_cache": kwargs.get("use_cache", True),
        }

    # ---- beam search 等で必要：キャッシュの並び替え ----
    def _reorder_cache(
        self,
        past_key_values: Tuple[Tuple[Tensor]],
        beam_idx: Tensor,
    ) -> Tuple[Tuple[Tensor]]:
        # 各層の (k,v,...) をビーム順に並べ替え
        reordered: List[Tuple[Tensor, ...]] = []
        for layer_past in past_key_values:
            reordered.append(tuple(past_state.index_select(0, beam_idx) for past_state in layer_past))
        return tuple(reordered)
