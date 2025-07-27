import csv

fields=['Name', 'Branch']
rows=[['Nikhil', 'COE'], ['ABC','COE', '2']]

filename="university_records.csv"

with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(rows)
