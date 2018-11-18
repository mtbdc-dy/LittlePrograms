from PIL import Image


# 去黑点
def fill_hole(g):
    rgb = []  # 存一个位置 边缘一块地区的 灰度值
    li = []  # 侦测到的存噪点位置
    (w, h) = g.size  # 图形大小
    for x in range(w):
        for y in range(h):
            rgb.clear()
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                a = x + i
                b = y + j
                pos = (a, b)
                if a < 0 or a > w - 1:
                    continue
                if b < 0 or b > h - 1:
                    continue
                rgb.append(g.getpixel(pos))

            if sum(rgb) == 255 * 8:
                li.append((x, y))
    for item in li:
        g.putpixel(item, 255)
    return g


# 找出一块连通部分的四个边界
def find_border_point(g):
    def dfs(pic, a, b):
        nonlocal lx, ly
        (we, he) = pic.size
        posi = (a, b)
        if 0 <= a < we and 0 <= b < he and not pic.getpixel(posi):
            lx.append(a)
            ly.append(b)
            pic.putpixel(posi, 255)
            pic = dfs(pic, a - 1, b)
            pic = dfs(pic, a, b + 1)
            pic = dfs(pic, a + 1, b)
            pic = dfs(pic, a, b - 1)
        return pic

    (w, h) = g.size
    for i in range(w):
        for j in range(h):
            pos = (i, j)
            if not g.getpixel(pos):
                # print('pos:', pos)
                lx = list()
                ly = list()
                g = dfs(g, i, j)
                B = [min(lx), min(ly), max(lx)+1, max(ly)+1]
                return g, B
