from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


img1 = Image.new(mode="RGB", size=(59, 20), color=(255, 255, 255))
font1 = ImageFont.truetype("Lucida Grande.ttf", 23)
draw1 = ImageDraw.Draw(img1, mode="RGB")

for i in range(4):
    # 每循环一次,从a到z中随机生成一个字母或数字
    # 65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    # str把生成的数字转换成字符串
    char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])

    # 每循环一次重新生成随机颜色
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 把生成的字母或数字添加到图片上
    # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    draw1.text([i * 14 + 5, -6], char1, color1, font=font1)


with open("pic.jpg", "wb") as f:
    img1.save(f)
img1.show()

