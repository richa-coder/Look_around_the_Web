import requests
from bs4 import BeautifulSoup
url="http://www.shopping.com/homeandgarden-kitchen/products"
look_for_it=requests.get(url)
soup=BeautifulSoup(look_for_it.content)
links=soup.find_all("a")

for link in links:
    print "<a href='%s'>%s</a>" %(link.get("href"),link.text)
g_data=soup.find_all("body",{"id":"softProductized"})
print g_data
for item in g_data:
    print item.text
