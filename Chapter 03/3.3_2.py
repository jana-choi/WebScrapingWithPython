from urllib.request import urlopen
from urllib.request import urlparse
from bs4 import BeautifulSoup
import re

# 페이지에서 발견된 내부 링크를 모두 목록으로 만듭니다.
def getInternalLinks(bs, includeUrl):
    includeUrl = "{}://{}".format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []

    # / 로 시작하는 링크를 모두 찾습니다.
    for link in bs.findAll("a", href = re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startswith("/"):
                    internalLinks.append(includeUrl + link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    
    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bs, excludeUrl):
    externalLinks = []

    # 현재 URL 을 포함하지 않으면서 http 나 www 로 시작하는 링크를 모두 찾습니다.
    for link in bs.findAll("a", href = re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    
    return externalLinks

# 사이트에서 찾은 외부 URL 을 모두 리스트로 수집합니다.
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = "{}://{}".format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, "html.parser")

    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)


allIntLinks.add("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")
