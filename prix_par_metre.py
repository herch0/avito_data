import csv
import re

with open('data_avito.csv', newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=";", quotechar='"')
  header = True
  surface_total = 0
  prix_total = 0
  for row in csvreader:
    if header:
      header = False
      continue
    else:
      annee = row[0]
      mois = row[1]
      prix = row[3]
      surface = row[5]
      surface_nb = surface[0:-2]
      surface_total += surface
      prix_total += prix
    #end else
  #end for
  print(surface_total / )
