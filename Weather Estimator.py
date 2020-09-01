#importing required modules
import requests
from bs4 import BeautifulSoup
print("Weather temperature")
search=input("Enter the Place:") #user input place
search_new="Weather of "+search
url=f"https://www.google.com/search?&q={search_new}"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser") #creating soup of the search page
update=s.find("div",class_="BNeawe") 
print(search," is ",update.text) #geting text from parsed soup
