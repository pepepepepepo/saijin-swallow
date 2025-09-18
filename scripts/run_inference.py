from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "sshleifer/tiny-gpt2"  # まずは軽いモデルで確認

tok = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

prompt = "Hello from saijin-swallow!"
inputs = tok(prompt, return_tensors="pt")

out = model.generate(**inputs, max_new_tokens=40, do_sample=True, temperature=0.8)

# 重要: .tolist() と flush=True
print(tok.decode(out[0].tolist(), skip_special_tokens=True), flush=True)
