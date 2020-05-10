from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    # html = urlopen("http://www.pythonscraping.com/pages/error.html")
    # html = urlopen("http://www.pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print(e)    # 404 Page Not Found
except URLError as e:
    print("The server could not be found!")
else:
    print("It Worked!")
    bs = BeautifulSoup(html.read(), 'html.parser')
    # print(bs.h1)
    try:
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag was not found")
    else:
        print(badContent)