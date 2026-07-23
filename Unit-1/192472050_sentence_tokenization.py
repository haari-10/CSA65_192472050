import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer (Run only once)
nltk.download('punkt')

text = "Hello everyone. Welcome to NLP! Python is easy to learn. Let's start."

sentences = sent_tokenize(text)

print("Sentence Tokens:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")