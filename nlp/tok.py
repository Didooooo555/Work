import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

text = 'Hello! I am study NLP. It is very interesting.'

words = word_tokenize(text, language= 'english')
print('Words:', words)
print(len(words))

sent = sent_tokenize(text, language= 'english')
print('Sentences:', sent)
print(len(sent))