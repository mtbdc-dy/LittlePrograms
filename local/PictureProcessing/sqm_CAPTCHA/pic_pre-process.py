from PIL import Image
import myPackages.pic_processing as mp
import copy
import random

im = Image.open("examples_for_pre-process/6181.jpg")
(w, h) = im.size

# 获取每个像素点的RGB，如果三个都为0，即为白点
arr = list()
for x in range(w):
    tmp_p = list()
    for y in range(h):
        pos = (x, y)
        if im.getpixel(pos)[0] <= 80 and im.getpixel(pos)[1] <= 80 and im.getpixel(pos)[2] <= 80:
            tmp_p.append(1)
        else:
            tmp_p.append(0)
    arr.append(tmp_p)
for item in arr:
    print(item)

im = im.convert('1')
for x in range(w):
    for y in range(h):
        if arr[x][y] == 0:
            im.putpixel((x, y), 255)
        else:
            im.putpixel((x, y), 0)

zone = (1, 1, w-1, h-1)     # l t r b
im = im.crop(zone)

im = mp.fill_hole(im)
# im.show()
# 118, 28


# 分割图片
g = copy.deepcopy(im)
count_figures = 0
while count_figures < 4:
    g, B = mp.find_border_point(g)
    # g.show()
    print(B)
    delta = B[2]-B[0] + 1
    delta_y = B[3] - B[1] + 1
    if delta < 6 or delta_y < 6:
        continue

    if delta < 17:
        B[2] += int((17 - delta)/2)
        B[0] += int((17 - delta)/2) - 17 + delta

    if delta_y < 17:
        B[3] += int((17 - delta_y)/2)
        B[1] += int((17 - delta_y)/2) - 17 + delta_y
    print(B)
    print()
    if B[0] < 0:
        B[2] += (0 - B[0])
        B[0] = 0
    if B[1] < 0:
        B[3] + (0 - B[1])
        B[1] = 0
    if B[2] > w:
        B[0] -= (B[2] - w)
        B[2] = w
    if B[3] > h:
        B[1] -= (B[3] - w)
        B[3] = h
    tmp_pic = im.crop(B)    # 切的时候,会去尾
    # tmp_pic.show()

    with open("tmp_" + str(random.randint(10000, 99999)) + ".jpeg", "wb") as f:
        tmp_pic.save(f)
    count_figures += 1

