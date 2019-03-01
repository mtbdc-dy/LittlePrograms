import matplotlib.pyplot as plt
from PIL import Image
import threading
import myPackages.process_txt as mp
import os


picture_path = 'validateCode.jpeg'


def part1():
    img = plt.imread(picture_path)
    plt.ion()
    plt.imshow(img)
    plt.ioff()
    plt.show()
    # print(img)
    print(1)
    return


def part2():
    a = Image.open(picture_path)
    a.show()
    return


part1()
exit()
part2()
t = threading.Thread(target=part2)  # 创建线程
print('111')
t.setDaemon(True)   # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
t.start()
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







