from swallow_tokenizer import SwallowTokenizer
from swallow_model import SwallowModel

tokenizer = SwallowTokenizer.from_pretrained("tokyotech-llm/Gemma-2-Llama-SwaLow-8b-it-v0.1")
model = SwallowModel.from_pretrained("tokyotech-llm/Gemma-2-Llama-SwaLow-8b-it-v0.1")

messages = [{"role": "user", "content": "Who are you?"}]
inputs = tokenizer.apply_swallow_template(messages, add_generation_prompt=True)

outputs = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_new_tokens=40
)

response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
