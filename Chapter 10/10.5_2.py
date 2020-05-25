import requests
session = requests.Session()

params = {"username": "username", "password": "password"}
welcome_page = "http://pythonscraping.com/pages/cookies/welcome.php"
s = session.post(welcome_page, params)

print("Cookie is set to:")
print(s.cookies.get_dict())
print("Going to profile page...")

profile_page = "http://pythonscraping.com/pages/cookies/profile.php"
r = session.get(profile_page)
print(r.text)
