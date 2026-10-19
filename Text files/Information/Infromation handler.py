import csv
TXTfile = 'Information.txt'

Enter = input("search learning: ")

with open(TXTfile, 'r+') as Textfile:
    M = Textfile.read()
   
    if Enter in M:
        print("Enter key word")
        Enter = input("Enter: ")
        if Enter:
            Textfile.writelines('\n'+ Enter)        
    else:
        print(False)