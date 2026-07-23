from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Today is a beautiful day"

result = generator(prompt, max_length=40)

print(result)