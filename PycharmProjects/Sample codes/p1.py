import nltk
import re
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk import word_tokenize

def preprocessing(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]

	print(sentences)
f = open("/home/tanya/nltk_data/corpora/product_reviews_1/Canon_G3.txt","r").read()
preprocessing(f)

