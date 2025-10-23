from transformers import AutoTokenizer
from swallow_model import SwallowForCausalLM

def main():
    model_id = "google/gemma-2b-it"
    tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    model = SwallowForCausalLM.from_pretrained(
        model_id, device_map="auto", torch_dtype="auto"
    )

    prompt = "役割: 優しい日本語の対話アシスタント。\nユーザ: 最近疲れました。\nアシスタント:"
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True, top_p=0.95, temperature=0.7,
        repetition_penalty=1.05,
    )
    print(tok.decode(out[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
