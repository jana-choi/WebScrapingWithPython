from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

# images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])

# tags = bs.findAll(lambda tag: len(tag.attrs) == 2)
tags = bs.findAll(lambda tag: tag.get_text() == "Or maybe he\'s only resting?")
for t in tags:
    print(t)
