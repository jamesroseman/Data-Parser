import csv

lines = []
with open('output.txt','r') as f:
    for line in f.readlines():
        lines.append(line.strip())

with open('corrected.csv','w') as correct:
    writer = csv.writer(correct, dialect = 'excel')
    with open('input.csv', 'r') as mycsv:
        reader = csv.reader(mycsv)
        for row in reader:
            if row[0] in lines:
                writer.writerow(row)

