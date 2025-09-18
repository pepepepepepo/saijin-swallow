from transformers import AutoModelForCausalLM, AutoTokenizer

# 小さめモデルでまず動作確認
MODEL_NAME = "facebook/opt-125m"

def main():
    print(f"Loading model: {MODEL_NAME}")
    tok = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    prompt = "Hello from saijin-swallow!"
    inputs = tok(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=40, do_sample=True, temperature=0.8)
    text = tok.decode(outputs[0], skip_special_tokens=True)
    print("\n=== Generated ===")
    print(text)

if __name__ == "__main__":
    main()
