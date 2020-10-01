import csv
import os

#scanning the app folder for Title IDs

root = input('provide path to the app folder of your ps vita')
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
print(dirlist)

#program assumes the tsv file is in the same folder, since it's a bother imo to have to input two paths
filename = 'PSV_GAMES.tsv'
with open(filename) as tsvfile:
  reader = csv.DictReader(tsvfile, dialect='excel-tab')
      
  for directory in dirlist:
      for row in reader:
          if row['Title ID']==directory:
              print(row['Name'])
                
