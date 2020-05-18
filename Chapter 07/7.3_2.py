from urllib.request import urlopen
from io import StringIO
import csv

url = "http://pythonscraping.com/files/MontyPythonAlbums.csv"
data = urlopen(url).read().decode("ascii", "ignore")
dataFile = StringIO(data)

dictReader = csv.DictReader(dataFile)

print(dictReader)

for row in dictReader:
    # print(row)
    print("The album \"{}\" was released in {}".format(row["Name"], str(row["Year"])))
