import csv
import os

#reading the database file you pass to the program

root='/Volumes/Untitled/app'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
print(dirlist)

filename = input("please give path to the tsv file: ")
with open(filename) as tsvfile:
  reader = csv.DictReader(tsvfile, dialect='excel-tab')
      
  for directory in dirlist:
      for row in reader:
          if row['Title ID']==directory:
              print(row['Name'])
                
