from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "facebook/opt-125m"  # 小さめで動作確認用 (CPUでも可)

tok = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

prompt = "Hello from saijin-swallow!"
inputs = tok(prompt, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=40, do_sample=True, temperature=0.8)

# ここを修正: .tolist() を付ける
print(tok.decode(out[0].tolist(), skip_special_tokens=True))
