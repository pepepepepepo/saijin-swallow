from transformers import GemmaPreTrainedModel, GemmaModel
import torch.nn as nn

class SwallowModel(GemmaPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.model = GemmaModel(config)
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)
        self.post_init()

    def forward(self, input_ids=None, attention_mask=None, **kwargs):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, **kwargs)
        hidden_states = outputs[0]
        logits = self.lm_head(hidden_states)
        return logits
