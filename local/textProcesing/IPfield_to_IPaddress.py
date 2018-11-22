import csv
import xlrd


def convert(s):
    if not s:
        return '', ''
    else:
        ip_s = s.split('/')[0]
        mask = s.split('/')[1]
        ip_a = ip_s.split('.')[0]
        ip_b = ip_s.split('.')[1]
        ip_c = ip_s.split('.')[2]
        # ip_d = ip_s.split('.')[3]
        # print(ip_s, mask)
        ip_e = ''
        if mask == '24':
            ip_e = ip_a + '.' + ip_b + '.' + ip_c + '.' + '255'
        if mask == '22':
            ip_e = ip_a + '.' + ip_b + '.' + str(int(ip_c) + 3) + '.' + '255'
        return ip_s, ip_e


def check_continuity(e, s):
    if not e or not s:
        return False

    if int(e.split('.')[2]) + 1 == int(s.split('.')[2]):
        return True


filename = 'bras地址.xlsx'
f = xlrd.open_workbook(filename)

filename_output = 'bras地址.csv'
g = open(filename_output, 'w', newline='')
writer = csv.writer(g)


table = f.sheet_by_name("Sheet1")
nrows = table.nrows
for i in range(nrows):
    print()
    row = table.row_values(i)
    print(row)
    line = [row[0]]
    ips, ipe = convert(row[1])
    line.append(ips)
    line.append(ipe)

    ips, ipe = convert(row[2])
    line.append(ips)
    line.append(ipe)

    ips, ipe = convert(row[3])
    line.append(ips)
    line.append(ipe)
    print(line)
    for j, k in [(2, 3), (2, 5), (4, 1), (4, 5), (6, 1), (6, 3)]:

        if check_continuity(line[j], line[k]):
            line[j] = line[k+1]
            del line[k+1]
            line.remove(line[k])
            break
    print(line)
    if len(line) == 3:
        writer.writerow(line)
    elif len(line) == 5:
        new_line1 = [line[0], line[1], line[2]]
        new_line2 = [line[0], line[3], line[4]]
        writer.writerow(new_line1)
        writer.writerow(new_line2)
    elif len(line) == 7:
        new_line1 = [line[0], line[1], line[2]]
        new_line2 = [line[0], line[3], line[4]]
        new_line3 = [line[0], line[5], line[6]]
        writer.writerow(new_line1)
        writer.writerow(new_line2)
        writer.writerow(new_line3)
    else:
        print('wrong')
