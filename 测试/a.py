import math
import myPackages.process_txt as mp
import os
import sys

# 当前文件绝对路径
print(os.path.dirname(os.path.abspath(__file__)))

print(int(1/2))
mp.show_path()  # D:\PyProjects\LittlePrograms\测试
a = 1
b = 2
# a, b = b, a
b, a = a, b
print(a, b)
print(os.getcwd())
print(pow(10, -0.5))

a = [1, 2, 0]
if all(a):
    print('True')







