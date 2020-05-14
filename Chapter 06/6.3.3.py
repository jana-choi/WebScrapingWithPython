# MySql 비밀번호 변경 명령문
# ALTER user '유저이름'@'localhost' IDENTIFIED WITH mysql_native_password BY '변경할비밀번호';

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3307, db='mysql') # port=3307 추가해야 접속 가능
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id = 3")
print(cur.fetchone())
cur.close()
conn.close()
