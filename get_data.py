from bs4 import BeautifulSoup as bs4

import requests
import re
import time
import datetime
import csv

def get_details_apprt(url):
	r_details = requests.get(url)
	html = bs4(r_details.text, 'html.parser')
	titre = re.sub('\s+', ' ', html.select('.page-header.mbm')[0].text)
	prix = html.select('.vi-price-label .amount')
	if len(prix) == 0:
		return None
	prix = prix[0]['title']
	aside_infos = html.select('aside.panel.panel-body.panel-info')[0].text
	m = re.match(r'.*?Nombre de pièces: ([0-9]+).*?', aside_infos, re.DOTALL)
	if m:
		nb_pieces = m.group(1)

	m = re.match('.*?Surface: (.*? m²).*?', aside_infos, re.DOTALL)
	if m:
		surface = m.group(1)
	m = re.match(r'.*?Secteur: ([\w_-]+).*?', aside_infos, re.DOTALL)
	if m:
		secteur = m.group(1)
	m = re.match(r".*?Adresse: ([\w'_\s-]+).*?Type", aside_infos, re.DOTALL)
	if m:
		adresse = re.sub(r"\s+", " ", m.group(1))

	date = html.select('.date.dtstart.value')[0]['title']
	annee_mois = extract_date_infos(date)
	annee = annee_mois[0]
	mois = annee_mois[1]
	annonce_details = {'titre': titre, 'prix': prix, 'nb_pieces': nb_pieces, 'surface': surface, 'secteur': secteur, 'adresse': adresse, 'annee': annee, 'mois': mois}
	return annonce_details
#end get_details_apprt

def extract_date_infos(dt):
	dt = re.sub('T', ' ', dt)
	dt_obj = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
	return (dt_obj.year, dt_obj.month)
#end extract_date_infos


with open('data_avito.csv', 'w', newline='') as csvfile:
	fields = ['annee', 'mois', 'titre', 'prix', 'nb_pieces', 'surface', 'secteur', 'adresse']
	csvwriter = csv.DictWriter(csvfile, fieldnames=fields, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
	csvwriter.writeheader()	

	for i in range(293):
		url = "http://www.avito.ma/fr/maroc/?ca=15&q=&cg=1010&w=1005&st=s&m=&m=&spr=&mpr=&o="+str(i+1)
		print(url)
		r = requests.get(url, allow_redirects=False)
		html = bs4(r.text, 'html.parser')
		liens = html.select('.panel-main.no-border-radius .item-info.ctext1.mls h2 a')
		for lien in liens:
			try:
				details = get_details_apprt(lien['href'])
				csvwriter.writerow(details)
				csvwriter.flush()
			except Exception:
				continue
			time.sleep(5)

print("------------------- FIN ------------------")
