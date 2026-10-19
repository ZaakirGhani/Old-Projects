import csv

ROW = []

file_Directory = 'Product - Name.csv'



with open(file_Directory, mode='r') as Reader:
    read = csv.DictReader(Reader)
    
    for row in read:
        if row['Name']:
            row['Name'] = 'Nathan'
            row['Product'] = 'Computer'
        ROW.append(row)


file = open(file_Directory,mode='a',newline='')
fieldnames = ['Name', 'Product']
Writer = csv.DictWriter(file,fieldnames=fieldnames)

Writer.writerows(ROW)