from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read("word/document.xml")

# print(xml_content.decode("utf-8"))

wordObj = BeautifulSoup(xml_content.decode("utf-8"))
textStrings = wordObj.findAll("w:t")

print("========================================================================")
# for textElem in textStrings:
#     print(textElem.text)

for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        # 출력할 태그가 없습니다.
        pass
    print(textElem.text)
    print(closeTag)
