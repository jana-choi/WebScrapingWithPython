# <h2>Tell me your name!</h2>
# <form method="post" action="processing.php">
# First name: <input type="text" name="firstname"><br>
# Last name: <input type="text" name="lastname"><br>
# <input type="submit" value="Submit" id="submit">
# </form>

import requests

params = {"firstname":"Ryan", "lastname":"Mitchell"}
r = requests.post("http://pythonscraping.com/pages/processing.php", data=params)
print(r.text)
