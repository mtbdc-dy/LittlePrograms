import csv
import re

filename = 'input' + '.csv'
file_output = 'output' + '.csv'
flag = True
m = re.compile('.*100\.64\..*', re.I)

g = open(file_output, 'w')
writer = csv.writer(g)
with open(filename,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        if flag == True:
            writer.writerow(row)
            flag = False
        elif m.match(row[27]):
                writer.writerow(row)






