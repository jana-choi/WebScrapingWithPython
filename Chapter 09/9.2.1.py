import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3307, user="root", passwd="root", db="mysql", charset="utf8")
cur = conn.cursor()
cur.execute("USE wikipedia")

def getUrl(pageId):
    cur.execute("SELECT url FROM pages WHERE id = %s", (int(pageId)))
    return cur.fetchone()[0]

def getLinks(fromPageId):
    fromId = int(fromPageId)
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromId))
    if cur.rowcount == 0:
        return []
    return [x[0] for x in cur.fetchall()]

def searchBreadth(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            if link == targetPageId:
                return path + [link]
            else:
                newPaths.append(path+[link])
    return searchBreadth(targetPageId, newPaths)


nodes = getLinks(1)
# 2866 | /wiki/British_Empire
targetPageId = 2866
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
    print(getUrl(pageId))
