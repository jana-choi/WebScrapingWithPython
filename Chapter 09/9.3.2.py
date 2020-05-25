from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Hear is some not very interesting text")
text = Text(tokens)
print(text)
