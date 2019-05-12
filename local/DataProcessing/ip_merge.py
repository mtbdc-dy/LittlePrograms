from IPy import IP
import xlrd


filename = 'ip.xlsx'
f = xlrd.open_workbook(filename)  # 打开excel
table = f.sheet_by_name("Sheet1")   # 打开sheet
nrows = table.nrows     # sheet的行数
print(nrows)

net_list = list()
for i in range(nrows):
    # print(table.row_values(i)[0])
    net_list.append(IP(table.row_values(i)[0]))

while True:
    count = 0
    for i in range(len(net_list)):
        try:
            net_list[i] += net_list[i+1]
        except:
            count += 1
            continue
        net_list.pop(i+1)

    if count == len(net_list):
        break

print(net_list)


