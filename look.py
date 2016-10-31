import requests
from bs4 import BeautifulSoup
url="http://www.shopping.com/homeandgarden-kitchen/products"
look_for_it=requests.get(url)
soup=BeautifulSoup(look_for_it.content)
links=soup.find_all("a")

for link in links:
    print "<a href='%s'>%s</a>" %(link.get("href"),link.text)
mydata=soup.find_all("body",{"id":"softProductized"})
print mydata
for item in mydata:
    print item.text
