from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

font1 = ImageFont.truetype("Lucida_Sans_Typewriter_Regular.ttf", 20)     # 字体 大小

for n in range(100):
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
    print("trainImage/" + tmp + ".jpeg")
    with open("trainImage/" + tmp + ".jpeg", "wb") as f:
        img1.rotate(random.randint(-40, 40), fillcolor='white').save(f)
    # img1.show()

