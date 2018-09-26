from PIL import Image


"""
过了好久全忘了
"""


def nine_squares(g):
    rgb = []  # 存一个位置 边缘一块地区的 灰度值
    li = []  # 侦测到的存噪点位置
    li2 = []
    (w, h) = g.size  # 图形大小
    for x in range(w):
        for y in range(h):
            rgb.clear()

            for i in range(-1, 2):
                for j in range(-1, 2):
                    a = x + i
                    b = y + j
                    pos = (a, b)

                    if a < 0 or a > w - 1:
                        continue
                    if b < 0 or b > h - 1:
                        continue
                    rgb.append(g.getpixel(pos))

            # 中间的点
            if len(rgb) == 9:
                mean = sum(rgb) / len(rgb)
                if mean < 90:  # 去除白点 255/9 = 28.33 9格里只有一个白点 30 60 90
                    li.append((x, y))
                    # g.putpixel((x, y), 0)

                if mean > 190:  # 去除黑点 255*8/9 = 226.67 9格里只有一个黑点 220 190
                    # g.putpixel((x, y), 0)
                    li2.append((x, y))
                    # g.putpixel((x, y), 255)

                # 边上的点
            if len(rgb) == 6:
                mean = sum(rgb) / len(rgb)
                if mean < 100:  # 去除白点 255/6 = 42.5 6格里只有一个白点 50 100
                    li.append((x, y))
                    # g.putpixel((x, y), 0)

                if mean > 210:  # 去除黑点 255*5/6 = 212.5 6格里只有一个黑点 210 160
                    # g.putpixel((x, y), 0)
                    li2.append((x, y))
                    # g.putpixel((x, y), 255)

    # 所有点检测完之后，再去除噪点
    for item in li:
        g.putpixel(item, 0)
    for item in li2:
        g.putpixel(item, 255)
    return g


def show_zero_image(g):
    (w, h) = g.size
    for j in range(h):
        for i in range(w):
            if g.getpixel((i, j)) == 0:
                print('0', end=' ')
            else:
                print(' ', end=' ')
        print('')
    g.show()


if __name__ == '__main__':
    # 图像二值化，去椒盐噪点
    for n in range(1, 10):
        # 打开图片
        n = 0
        im = Image.open("GGDXLT_Examples/validateCode" + str(n) + ".jpeg")

        # 切割边框
        (w, h) = im.size    # 获得图片长和宽
        zone = (2, 1, w-2, h-1)     # 左下角和右下角的坐标
        cropIm = im.crop(zone)

        # 转化图片
        # g = cropIm.convert('L')   # 转化为灰度图
        g = cropIm.convert('1')   # 转化为二值化图 0为黑色 or 255为白色
        g.show()

        # 检测噪点
        gn = nine_squares(g)
        # show_zero_image(gn)
        gnn = nine_squares(gn)
        show_zero_image(gnn)
        break






