from PIL import Image
import numpy as np
import tensorflow as tf
import copy
import random
import os

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


# 切割sqm验证码
def cut_sqm_captcha(image):
    print('def mp.cut_sqm_captcha:')
    im = image
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
    # for item in arr:
    #     print(item)

    im = im.convert('1')
    for x in range(w):
        for y in range(h):
            if arr[x][y] == 0:
                im.putpixel((x, y), 255)
            else:
                im.putpixel((x, y), 0)

    zone = (1, 1, w - 1, h - 1)  # l t r b
    im = im.crop(zone)

    im = fill_hole(im)
    # im.show()
    # 118, 28

    # 分割图片
    g = copy.deepcopy(im)
    count_figures = 0
    np_arr = None
    while count_figures < 4:
        g, B = find_border_point(g)
        # g.show()
        print(B)
        delta = B[2] - B[0]
        delta_y = B[3] - B[1]
        if delta < 6 or delta_y < 6:
            continue
        B[2] += int((16 - delta) / 2)
        B[0] += int((16 - delta) / 2) - 16 + delta
        B[3] += int((16 - delta_y) / 2)
        B[1] += int((16 - delta_y) / 2) - 16 + delta_y
        print(B)

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
        print(B)
        tmp_pic = im.crop(B)  # 切的时候,会去尾
        tmp_pic.show()
        print(tmp_pic.size)
        print()
        if np_arr is None:
            np_arr = np.array(tmp_pic, dtype=np.float32)
            np_arr.shape = (1, 256)
        else:
            np_arr_tmp = np.array(tmp_pic)
            np_arr_tmp.shape = (1, 256)
            np_arr = np.concatenate((np_arr, np_arr_tmp))

        count_figures += 1
    return np_arr


# 识别sqm验证码
def recognize_sqm_captcha(ndas):
    """
    SQM 验证码识别 （0~8）
    基于CNN实现纯数字识别。
    """
    print('def mp.recognize_sqm_captcha:')
    # input_pic = np.array(im, dtype=np.float32).reshape((1, 256))
    # print(input_pic)
    input_vec = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(os.path.dirname(os.path.abspath(__file__)) + '/ckpt/sqm/sqm.ckpt.meta')
        saver.restore(sess, os.path.dirname(os.path.abspath(__file__)) + '/ckpt/sqm/sqm.ckpt')
        pred = tf.get_collection('network-output')[0]

        graph = tf.get_default_graph()
        x = graph.get_operation_by_name('xs').outputs[0]
        y_ = graph.get_operation_by_name('ys').outputs[0]
        kp = graph.get_operation_by_name('kp').outputs[0]

        y = sess.run(pred, feed_dict={x: ndas, y_: input_vec, kp: 1})
        print(len(y))
        print([np.where(y[0] == max(y[0]))[0][0], np.where(y[1] == max(y[1]))[0][0],
               np.where(y[2] == max(y[2]))[0][0], np.where(y[3] == max(y[3]))[0][0]])
        return [np.where(y[0] == max(y[0]))[0][0], np.where(y[1] == max(y[1]))[0][0],
                np.where(y[2] == max(y[2]))[0][0], np.where(y[3] == max(y[3]))[0][0]]


