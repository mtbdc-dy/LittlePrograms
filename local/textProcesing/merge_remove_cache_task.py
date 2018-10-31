# -*- coding: utf-8 -*-
import os
import xlwt
import xlrd

if __name__ == '__main__':
    # 设定输出xls文件
    filename = 'eoms_remove_cache.xls'
    workbook_write = xlwt.Workbook(filename)
    ws = workbook_write.add_sheet('sheet01')
    row = 1

    path = os.getcwd()
    print(path)
    fs = os.listdir(path + r'\eoms_remove_cache')
    print(fs)
    for task_sequence in fs:
        print(path + r'\eoms_remove_cache\\' + task_sequence)
        fs_sub = os.listdir(path + r'\eoms_remove_cache\\' + task_sequence)
        print(fs_sub)
        for excel in fs_sub:
            fr = xlrd.open_workbook(path + r'\eoms_remove_cache\\' + task_sequence + '\\' + excel)
            sheet = fr.sheet_by_index(0)
            nrows = sheet.nrows
            for i in range(nrows):
                rows = sheet.row_values(i)
                rows[0] = task_sequence
                for j in range(len(rows)):
                    ws.write(row, j, rows[j])
                row += 1

    workbook_write.save(filename)


