import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs = BeautifulSoup(html, "html.parser")

# 비교 테이블은 현재 페이지의 첫 번째 테이블 입니다.
table = bs.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("editor.csv", "wt+")
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        try:
            writer.writerow(csvRow)
        except Exception as e:
            print(e)
finally:
    csvFile.close()
