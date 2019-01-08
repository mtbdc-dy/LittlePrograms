import csv
import xlrd
from IPy import IP
import myPackages.ip as mi

"""
    将IP地址段转化成IP_start - IP_end 的形式
    要求：
        0、读文件，规范模板（Bras地址整理.xlsx）
        1、合并同bras的ip地址
        2、将输出转换成中兴，华为所需样式
"""


if __name__ == '__main__':

    filename = 'Bras地址整理.xlsx'
    f = xlrd.open_workbook(filename)
    filename_output = 'bras地址_hw.csv'
    g = open(filename_output, 'w', newline='')
    writer_hw = csv.writer(g)
    filename_output = 'bras地址_zte.csv'
    h = open(filename_output, 'w', newline='')
    writer_zte = csv.writer(h)

    table = f.sheet_by_name("Sheet1")
    nrows = table.nrows
    print(nrows)
    csv_content = []
    for i in range(nrows):
        if i == 0:
            continue

        row = table.row_values(i)
        if row[0] != '':
            print(row)
            bras = row[0]
            try:
                ip_unique = IP(row[2])
            except:
                ip_unique = IP('0.0.0.0')
            ip_shared = IP(row[4])
        else:
            # print(row)
            ip_shared_sec = IP(row[4])
            try:
                ip_shared = ip_shared + ip_shared_sec
                # print(ip_shared)
                writer_hw.writerow([bras, ip_shared.strNormal(2)])
                writer_zte.writerow([bras, ip_shared.strNormal(3)])
            except:
                writer_hw.writerow([bras, ip_shared.strNormal(2), ip_shared_sec.strNormal(2)])
                if mi.add_one_on_ip(str(ip_shared[-1])) == str(ip_shared_sec[0]):
                    writer_zte.writerow([bras, str(ip_shared[0]) + '-' + str(ip_shared_sec[-1])])
                elif str(ip_shared[0]) == mi.add_one_on_ip(str(ip_shared_sec[-1])):
                    writer_zte.writerow([bras, str(ip_shared_sec[0]) + '-' + str(ip_shared[-1])])
                else:
                    writer_zte.writerow([bras, ip_shared.strNormal(3), ip_shared_sec.strNormal(3)])



