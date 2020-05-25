# <h2>Upload a file!</h2>
# <form action="processing2.php" method="post" enctype="multipart/form-data">
#   Submit a jpg, png, or gif: <input type="file" name="uploadFile"><br>
#   <input type="submit" value="Upload File">
# </form>

import requests

files = {"uploadFile": open("files/Python-logo.jpg", "rb")}
url = "http://pythonscraping.com/pages/processing2.php"
r = requests.post(url, files=files)
print(r.text)
