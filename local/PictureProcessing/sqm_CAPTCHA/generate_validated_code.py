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

# arr = np.empty((1, 256), dtype=np.float32)
# print(arr)
arr = None
for n in range(100000):
    if n % 1000 == 0:
        print(n)
    img1 = Image.new(mode="1", size=(16, 16), color='white')
    draw1 = ImageDraw.Draw(img1)

    # 每循环一次,从a到z中随机生成一个字母或数字
    # 65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    # str把生成的数字转换成字符串
    char1 = random.choice([str(random.randint(0, 8))])

    # 每循环一次重新生成随机颜色

    # 把生成的字母或数字添加到图片上
    # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    tmp = char1
    x = random.randrange(-1, 1)
    y = random.randrange(-1, 1)
    draw1.text([2 + x, -5 + y], char1, 'black', font=font1)
    # img1.show()
    img1 = img1.rotate(random.randint(-45, 45), resample=Image.BICUBIC, fillcolor='white')
    # print(img1.getpixel((1, 1)))
    # 16 x 16 = 256

    # img1.show()

    if arr is None:
        arr = np.array(img1, dtype=np.float32).reshape(1, 256).tolist()
        arr[-1].append(float(char1))
    else:
        arr.append(np.array(img1, dtype=np.float32).reshape(1, 256).tolist()[0])
        arr[-1].append(float(char1))


    # if n == 2:
    #     print(arr)
    #     exit()

    # print(type(arr))

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
# np.save("test_group.npy", arr)
np.save("train_group.npy", np.array(arr, dtype=np.float32))

