import csv

filename="C:/Gracy_Info/Hexaware/Python Foundation Training - Batch 2/Python/Python programs/File handling/info.csv"
rows, fields=[],[]

with open(filename, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))

print('Field names are: '+ ", ".join(field for field in fields))
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" ")
    print('\n')
