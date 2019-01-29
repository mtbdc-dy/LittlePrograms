import xlrd  # 读excel
import xlwt  # 写excel

# '''写 excel start'''
# filename = 'desc.xlsx'
# f = xlwt.Workbook(filename)  # 打开excel
# ws = f.add_sheet('sheet_name')  # 新建一个sheet
# for i in range(10):
#     ws.write(i, i, i)
# f.save(filename)
# '''写 excel end'''
#
#
# '''读excel start'''
# filename = 'desc.xlsx'    # 文件名
#
# f = xlrd.open_workbook(filename)    # 打开excel
# table = f.sheet_by_name("sheet_name")   # 打开sheet
# nrows = table.nrows     # sheet的行数
# print(nrows)
#
# for i in range(nrows):
#     rows = table.row_values(i)  # 读第i行
#     print(rows)
# '''读excel end'''


if __name__ == '__main__':
    filename = 'Bras地址整理.xlsx'    # 文件名

    f = xlrd.open_workbook(filename)    # 打开excel
    table = f.sheet_by_name("Sheet1")   # 打开sheet
    nrows = table.nrows     # sheet的行数
    print(nrows)

    for i in range(nrows):
        rows = table.row_values(i)  # 读第i行
        print(rows)


