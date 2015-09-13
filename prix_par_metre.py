import csv
import re

with open('apprt_casa.csv', newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=";", quotechar='"')
  header = True
  prix_metre_total = 0
  prix_metre_secteur = {}
  nb = 0
  for row in csvreader:
    if header:
      header = False
      continue
    else:
      nb+=1
      annee = row[0]
      mois = row[1]
      prix = int(row[3])
      surface = row[5]
      secteur = row[6]
      surface_nb = int(surface[0:-2])
      prix_metre = prix/surface_nb;
      prix_metre_total += prix_metre
      if secteur in prix_metre_secteur:
        prix_metre_secteur[secteur].append(prix_metre)
      else:
        prix_metre_secteur[secteur] = [prix_metre]
    #end else
  #end for
print("moyenne total", prix_metre_total/nb)
with open('prix_par_metre_casa.csv', 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=';')
  for secteur, val in prix_metre_secteur.items():
    nb_ann = len(val)
    prix_total_secteur = 0
    for prix in val:
      prix_total_secteur += prix
    moyenne = prix_total_secteur / nb_ann
    if nb_ann > 10:
      print(secteur, moyenne, nb_ann)
      csvwriter.writerow([secteur, moyenne, nb_ann])
