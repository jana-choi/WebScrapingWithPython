# from nltk.book import *
from nltk import word_tokenize
from nltk import pos_tag

# text = word_tokenize("Strange women lying in ponds distributing swords "
#                     "is no basis for a system of goverment.")

text = word_tokenize("The dust was thick so he had to dust")

words = pos_tag(text)
print(words)
