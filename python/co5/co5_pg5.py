import csv
fields=['Names','Branch','Year','CGPA']
rows=[['nilk','coe','2','9.0'],
      ['vilka','coe','2','7.0']]
filename="university_records.csv"
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter .writerow(fields)
    csvwriter.writerows(rows)
