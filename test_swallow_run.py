# test_swallow_run.py

from transformers import AutoTokenizer
from swallow_model import SwallowForCausalLM  # ✅ 修正済み

def test_swallow_generate():
    model_id = "google/gemma-2b-it"
    tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    model = SwallowForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")

    prompt = "こんにちは、自己紹介して。"
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=64,
        do_sample=True, top_p=0.9, temperature=0.7,
    )
    result = tok.decode(out[0], skip_special_tokens=True)
    print("🧪 SwallowForCausalLM output:", result)
    assert len(result) > 0
