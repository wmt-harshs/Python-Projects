
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter github user name:- ")

url = "https://github.com/" + github_user

r = requests.get(url)
s = bs(r.content, "html.parser")
profile_image = s.find("img",{"alt":"Avatar"})["src"]
print(profile_image)