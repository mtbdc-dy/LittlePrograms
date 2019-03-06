import xlrd  # 读excel
import xlwt  # 写excel
from xlutils.copy import copy

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
    filename = 'desc.xlsx'    # 文件名

    f = xlrd.open_workbook(filename, formatting_info=True)    # 打开excel
    wb = copy(f)
    table = wb.get_sheet(0)
    ws = wb.get_sheet(0)
    wb.save('excel_copy_hello.xls')
    exit()
    # table = f.sheet_by_name("Sheet1")   # 打开sheet
    nrows = table.nrows     # sheet的行数
    print(nrows)

    for i in range(nrows):
        rows = table.row_values(i)  # 读第i行
        print(rows)


