from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

output = generator("The future of AI", max_length=40)

print(output)