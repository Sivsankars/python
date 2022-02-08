import csv
listof=[]
with open('university_records.csv') as obj:
    fobj=csv.reader(obj)
    for rows in fobj:
        print(rows)

