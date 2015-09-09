from bs4 import BeautifulSoup as bs4
import requests
import re
import time
import datetime

def get_details_apprt(url):
	r_details = requests.get(url)
	html = bs4(r_details.text, 'html.parser')
	titre = re.sub('\s+', ' ', html.select('.page-header.mbm')[0].text)
	print('titre: ' + titre)
	prix = html.select('.vi-price-label .amount')
	if len(prix) == 0:
		return None
	prix = prix[0]['title']
	print('prix: ' + prix)
	aside_infos = html.select('aside.panel.panel-body.panel-info')[0].text
	m = re.match(r'.*?Nombre de pièces: ([0-9]+).*?', aside_infos, re.DOTALL)
	if m:
		nb_pieces = m.group(1)
		print('nb pieces: ' + nb_pieces)

	m = re.match('.*?Surface: (.*? m²).*?', aside_infos, re.DOTALL)
	if m:
		surface = m.group(1)
		print('surface: ' + surface)
	m = re.match(r'.*?Secteur: ([\w_-]+).*?', aside_infos, re.DOTALL)
	if m:
		secteur = m.group(1)
		print('secteur: ' + secteur)

	m = re.match(r".*?Adresse: ([\w'_\s-]+).*?Type", aside_infos, re.DOTALL)
	if m:
		adresse = re.sub(r"\s+", " ", m.group(1))
		print('adresse: ' + adresse)

	date = html.select('.date.dtstart.value')[0]['title']
	print(date)
	print('date: ' + extract_date_infos(date)[0])

def extract_date_infos(dt):
	dt = re.sub('T', ' ', dt)
	t_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
	print('extract_date_infos ' + dt)
	print("apres")
	print('date object ' + dt_obj)
	return (dt_obj.year, dt_obj.month)

url = "http://www.avito.ma/fr/maroc/?ca=15&q=&cg=1010&w=1005&st=s&m=&m=&spr=&mpr="

r = requests.get(url, allow_redirects=False)

html = bs4(r.text, 'html.parser')

liens = html.select('.panel-main.no-border-radius .item-info.ctext1.mls h2 a')

for lien in liens:
	time.sleep(5)
	try:
		get_details_apprt(lien['href'])
	except Exception:
		continue#répéter plutot
