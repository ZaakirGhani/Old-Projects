#Testing
import csv
rowss = []
with open ('D.csv', 'r+') as D:
    Dreader = csv.DictReader(D)
    
    for row in Dreader:
        rowss.append(row)
    if rowss:
        with open ('D.csv', 'w') as D:
            fieldnames = rowss[0].keys()
            Dwriter = csv.DictWriter(D, fieldnames=fieldnames)

            print(fieldnames)
    