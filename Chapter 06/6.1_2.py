import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    print("===================== getAbsoluteURL =====================")
    print("#### baseUrl: {}".format(baseUrl))
    print("#### source: {}".format(source))

    if source.startswith("http://www."):
        url = "http://{}".format(source[11:])
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://{}".format(url)
    else:
        url = "{}/{}".format(baseUrl, source)
    
    print("#### url: {}".format(url))

    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    print("===================== getDownloadPath =====================")
    print("#### baseUrl: {}".format(baseUrl))
    print("#### absoluteUrl: {}".format(absoluteUrl))
    print("#### downloadDirectory: {}".format(downloadDirectory))

    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path

    directory = os.path.dirname(path)

    print("#### path: {}".format(path))
    print("#### directory: {}".format(directory))

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path


html = urlopen("http://www.pythonscraping.com")
bs = BeautifulSoup(html, "html.parser")
downloadList = bs.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print("★★★ fileUrl: {}".format(fileUrl))
        try:
            urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
        except Exception as e:  # 예외 처리 추가
            print(e)
