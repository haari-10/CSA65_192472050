from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = "Machine learning is powerful."

tokens = tokenizer.tokenize(sentence)

print(tokens)