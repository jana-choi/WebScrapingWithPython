from nltk.book import *

print("### len(text6) / len(set(text6))\n", len(text6) / len(set(text6)))

from nltk import FreqDist

fdist = FreqDist(text6)
print("### fdist.most_common(10)\n", fdist.most_common(10))

from nltk import bigrams

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print("### bigramsDist[(\"Sir\", \"Robin\")]\n", bigramsDist[("Sir", "Robin")])

from nltk import ngrams

fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print("### fourgramsDist[(\"father\", \"smelt\", \"of\", \"elderberries\")]\n", fourgramsDist[("father", "smelt", "of", "elderberries")])

fourgrams = ngrams(text6, 4)
print("****** coconut ******")
for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)
