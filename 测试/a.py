import matplotlib.pyplot as plt
from PIL import Image
import threading

import myPackages.process_txt as mp
import os
import sys

picture_path = 'validateCode.jpeg'
s = '中兴'
S = s.encode('GBK')
print(S)
x = b'\xd6\xd0\xd0\xcb\x69\x43\x61\x63\x68\x65\x3d\xd6\xd0\xd0\xcb\xbb\xba\xb4\xe6\xbc\xd3\xcb\xd9\xcd\xf8\xc2\xe7'
X = x.decode('GBK')
print(X)
exit()
def part1():
    img = plt.imread(picture_path)
    plt.imshow(img)
    plt.show()
    print(img)
    # plt.ion()
    return


def part2():
    a = Image.open(picture_path)
    a.show()
    return


# Part1 plt
# Part2 Image
part1()
part2()
t = threading.Thread(target=part2)  # 创建线程
print('111')
t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
t.start()

part2()
exit()

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







