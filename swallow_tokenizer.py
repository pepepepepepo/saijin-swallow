from transformers import GemmaTokenizer

class SwallowTokenizer(GemmaTokenizer):
    def apply_swallow_template(self, messages, add_generation_prompt=True):
        # 誠人の語温構造に合わせたテンプレートをここに定義
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"<|user|>{content}\n"
            elif role == "assistant":
                prompt += f"<|assistant|>{content}\n"
        if add_generation_prompt:
            prompt += "<|assistant|>"
        return self(prompt, return_tensors="pt")
