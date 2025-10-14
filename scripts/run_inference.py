import time, torch, sys
print(">>> START run_inference.py", "torch", torch.__version__, "cuda?", torch.cuda.is_available(), flush=True)

print(">>> building tokenizer & model for", MODEL_NAME, flush=True)
tok = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

print(">>> prepare inputs", flush=True)
prompt = "Hello from saijin-swallow!"
inputs = tok(prompt, return_tensors="pt")

print(">>> generate() start", flush=True)
t0 = time.time()
out = model.generate(**inputs, max_new_tokens=40, do_sample=True, temperature=0.8)
print(">>> generate() done in", round(time.time()-t0, 3), "sec", flush=True)

print(tok.decode(out[0].tolist(), skip_special_tokens=True), flush=True)
print(">>> END", flush=True)

from transformers import AutoModelForCausalLM, AutoTokenizer

