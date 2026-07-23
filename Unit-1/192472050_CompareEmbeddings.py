from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

s1 = tokenizer("I like Python.", return_tensors="pt")
s2 = tokenizer("Python is my favorite language.", return_tensors="pt")

o1 = model(**s1)
o2 = model(**s2)

print(o1.last_hidden_state.shape)
print(o2.last_hidden_state.shape)