import json
from urllib.request import urlopen

def getCouontry(ipAddress):
    url = "http://api.ipstack.com/" + ipAddress
    url += "?access_key=ACCESS_KEY&amp;format=1"

    response = urlopen(url).read().decode("utf-8")
    responseJson = json.loads(response)
    
    return responseJson.get("contry_code")


print(getCouontry("50.78.253.58"))
