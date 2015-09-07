from bs4 import BeautifulSoup as bs4
import requests
import re
import time

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
#	print("+++",aside_infos,"+++")
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
	print('date: ' + date)

def get_details_voitures(url):
	r_details = request.get(url)
	html = bs4(r_details.text, 'html.parser')
	prix = html.select('.price-header .amount')['title']
	aside_infos = html.select('.date.dtstart.value').text
	m = re.match('<h2 class="font-normal fs12 no-margin ln22"><strong>Année-Modèle:</strong> (\d)</h2>', aside_infos)
	if m:
		annee_modele = m.group(1)
	m = re.match('<h2 class="font-normal fs12 no-margin ln22"><strong>Kilométrage:</strong> ([\d\s-])</h2>', aside_infos)
	if m:
		kilometrage = m.group(1)
	m = re.match('<h2 class="font-normal fs12 no-margin ln22"><strong>Type de carburant:</strong> ([\d\s-])</h2>', aside_infos)
	if m:
		carburant = m.group(1)

	m = re.match('<h2 class="font-normal fs12 no-margin ln22"><strong>Marque:</strong> ([\d\s-])</h2>', aside_infos)
	if m:
		marque = m.group(1)

	m = re.match('<h2 class="font-normal fs12 no-margin ln22"><strong>Modèle:</strong> ([\d\s-])</h2>', aside_infos)
	if m:
		modele = m.group(1)
	date = html.select('.date.dtstart.value')['title']
	print(prix)

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
