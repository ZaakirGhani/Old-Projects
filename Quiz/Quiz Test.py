import csv

with open('Quiz Questions.csv','r') as Q:
    read = csv.DictReader(Q)

    for line in read:
        print(line['Quiz'])

with open('Quiz.txt', 'r') as Rea:
    read = csv.DictReader(Rea,delimiter=',')
    for line in read:
        print(line['N'])