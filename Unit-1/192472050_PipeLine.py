from transformers import pipeline

classifier = pipeline("sentiment-analysis")

print(classifier("Python is very easy to learn."))