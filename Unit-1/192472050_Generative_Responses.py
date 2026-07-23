from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning"
]

for prompt in prompts:
    result = generator(prompt, max_length=30)
    print("Prompt:", prompt)
    print(result)
    print()