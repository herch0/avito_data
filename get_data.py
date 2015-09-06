from bs4 import BeautifulSoup as bs4
import requests

url = "http://www.avito.ma/fr/maroc/?ca=15&q=&cg=5010&w=1005&st=s&m=&m=&spr=&mpr="


r = requests.get(url, allow_redirects=False)

html = bs4(r.text, 'html.parser')

#items = html.find_all('div', attrs={'class': 'li-hover'})
items = html.select('div.item.li-hover')

print(len(items))

#for item in items:
#	print(item)
