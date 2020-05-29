from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org{}".format(articleUrl))
    bs = BeautifulSoup(html, "html.parser")
    return bs.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # 개정 히스토리 페이지 형식은 다음과 같습니다.
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl += pageUrl + "&action=history"
    print("### history url is: {}".format(historyUrl))

    html = urlopen(historyUrl)
    bs = BeautifulSoup(html, "html.parser")

    # 클래스가 "mw-anonuserlink" 인, 사용자 이름이 아니라 IP 주소가 들어있는 링크만 찾습니다.
    ipAddresses = bs.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCouontry(ipAddress):
    try:
        url = "http://api.ipstack.com/" + ipAddress
        url += "?access_key=ACCESS_KEY&amp;format=1"
        response = urlopen(url).read().decode("utf-8")
    except HTTPError:
        return None
    
    responseJson = json.loads(response)
    return responseJson.get("contry_code")


links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("-"*20)
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCouontry(historyIP)
            if country is not None:
                print("{} is from {}".format(historyIP, country))
            else:
                print(historyIP)
    
    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
