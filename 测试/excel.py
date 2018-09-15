import xlrd

# excel 文件都
filename_output = '附件五、物联网HLR-ID（截至2018年2月）.xlsx'

f3 = xlrd.open_workbook(filename_output)
table = f3.sheet_by_name("Sheet1")
nrows = table.nrows
for i in range(nrows):
    rows  = table.row_values(i)
    # print(rows[0:1])

str = '123435'
print(str[0:2])

matrix = [[] for i in range(10)]

matrix[1].append('1')
matrix[1].append('1')
matrix[2].append('1')
print(matrix)
