import xlrd  # 读excel

"""
生成交换机配置命令
Description
"""

if __name__ == '__main__':

    filename = 'desc.xlsx'  # 文件名

    f = xlrd.open_workbook(filename)  # 打开excel

    sheets = f.sheets()

    for item in sheets:
        print(item.name)
        table = f.sheet_by_name(item.name)  # 打开sheet
        nrows = table.nrows  # sheet的行数
        # print(nrows)

        lines = list()
        for i in range(nrows):
            rows = table.row_values(i)  # 读第i行
            line = 'interface ' + str(rows[0]) + '\n'
            lines.append(line)
            line = 'description ' + str(rows[1]) + '\n'
            lines.append(line)

            g = open(item.name + '.txt', 'w')
            for l in lines:
                g.write(l)
            g.close()


