import requests
from bs4 import BeautifulSoup

link = 'https://timesofindia.indiatimes.com/mostread.cms?day=1'
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
headlines = []

for i in soup.find_all("div",{'class':'listing4 clearfix'}):
    for j in i.find_all("li"):
        k = j.text
        headlines.append(k)
print(headlines)
