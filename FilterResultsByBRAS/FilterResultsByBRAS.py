import csv
import re

filename = 'input' + '.csv'
file_output = 'output' + '.csv'

g = open(file_output, 'w')
writer = csv.writer(g)
flag = True

with open(filename,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        if flag:
            row = row + ['bras']
            writer.writerow(row)
            flag = False
        else:
            n = 64
            while n <= 127:
                m = re.compile('.*100\.' + str(n) + '\.0\.1.*', re.I)
                if m.match(row[27]):
                    row = row + [str(n)]
                    writer.writerow(row)
                n += 1










