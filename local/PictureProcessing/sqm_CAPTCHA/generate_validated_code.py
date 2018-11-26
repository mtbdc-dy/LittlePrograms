from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import numpy as np

"""
要有1000轮 每轮100个数据，也就是要 10万张图片 我觉得可以一边生成一边训练了=.=
还要有1000张测试图片
一共10.1万张图片
"""
font1 = ImageFont.truetype("Lucida_Sans_Typewriter_Regular.ttf", 20)     # 字体 大小

arr = np.empty((1, 256), dtype=np.float32)
print(arr)
for n in range(100000):
    img1 = Image.new(mode="RGB", size=(16, 16), color='white')
    draw1 = ImageDraw.Draw(img1)

    # 每循环一次,从a到z中随机生成一个字母或数字
    # 65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    # str把生成的数字转换成字符串
    char1 = random.choice([str(random.randint(0, 8))])

    # 每循环一次重新生成随机颜色

    # 把生成的字母或数字添加到图片上
    # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    draw1.text([2, -5], char1, 'black', font=font1)
    tmp = char1

    img1 = img1.rotate(random.randint(-45, 45), fillcolor='white').convert('1')
    # print(img1.getpixel((1, 1)))
    arr_tmp = np.array(img1)
    arr_tmp.shape = (1, 256)
    # arr = np.concatenate((arr, arr_tmp))
    # print(type(arr))
    print(arr)
    exit()
    # print("trainImage/" + str(n) + '_' + tmp + ".jpeg")
    # with open("trainImage/" + str(n) + '_' + tmp + ".jpeg", "wb") as f:
    #     img1 = img1.rotate(random.randint(-45, 45), fillcolor='white')
    #     img1.save(f)
    #     img1 = img1.convert('1')
    #     print(img1.getpixel((1, 1)))
    #     arr = np.array(img1)
    #     print(type(arr))
    #     print(arr)
    #     exit()


