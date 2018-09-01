from PIL import Image

# 图像二值化，去椒盐噪点
for n in range(1, 10):
    # 打开图片
    im = Image.open("GGDXLT_Examples/validateCode" + str(n) + ".jpeg")

    # 切割边框
    (w, h) = im.size
    zone = (2, 1, w-2, h-1)
    cropIm = im.crop(zone)

    # 转化图片
    # g = cropIm.convert('L')   # 转化为灰度图
    g = cropIm.convert('1')   # 转化为二值化图


    rgb = []    # 存一个位置 边缘一块地区的 灰度值
    li = []     # 侦测到的存噪点位置
    li2 = []
    (w, h) = g.size     # 图形大小
    for x in range(w):
        for y in range(h):
            pos = (x, y)
            rgb.clear()

            for i in range(-1, 2):
                for j in range(-1, 2):
                    a = x + i
                    b = y + j
                    pos = (a, b)

                    if a < 0 or a > w-1:
                        continue
                    if b < 0 or b > h-1:
                        continue
                    rgb.append(g.getpixel(pos))

            mean = sum(rgb)/len(rgb)
            if mean < 30:
                g.putpixel((x, y), 255)
            elif mean < 125:
                li.append((x, y))
            if mean > 570:
                g.putpixel((x, y), 0)
                li2.append((x, y))
                # g.putpixel((x, y), 255)

    for item in li:
        g.putpixel(item, 0)
    for item in li2:
        g.putpixel(item, 255)

    (w, h) = g.size
    for j in range(h):
        for i in range(w):
            if g.getpixel((i, j)) == 0:
                print('0', end=' ')
            else:
                print(' ', end=' ')
        print('')
    g.show()




