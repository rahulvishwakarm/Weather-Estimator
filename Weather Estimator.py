import requests
from bs4 import BeautifulSoup
print("Weather temperature")
search=input("Enter the Place:")
search_new="Weather of "+search
url=f"https://www.google.com/search?&q={search_new}"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
update=s.find("div",class_="BNeawe")
print(search," is ",update.text)
