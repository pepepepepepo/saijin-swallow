from transformers import GemmaTokenizer, GemmaForCausalLM

model_name = "tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1"

tokenizer = GemmaTokenizer.from_pretrained(model_name)
model = GemmaForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto",
    low_cpu_mem_usage=True,
    resume_download=True
)


messages = [{"role": "user", "content": "Who are you?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=40)
response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)

print(response)
