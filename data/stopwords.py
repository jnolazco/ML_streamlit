from nltk import tokenize, word_tokenize

with open("stopwords.txt", "r", encoding="utf-8") as f:
     text = " ".join(f.readlines())
STOP_WORDS = set(text.split())
print(STOP_WORDS)
