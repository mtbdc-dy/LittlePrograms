import numpy as np


def name2label(name):
    label = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
    print(len(label))
    for i, c in enumerate(name):
        if ord(c) < 58:
            idx = i * CHAR_SET_LEN + ord(c) - ord('0')      # 返回对用的ASCII 数值
            label[idx] = 1
        else:
            idx = i * CHAR_SET_LEN + ord(c) - ord('A') + 10  # 返回对用的ASCII 数值
            label[idx] = 1
    return label


if __name__ == '__main__':
    MAX_CAPTCHA = 4
    CHAR_SET_LEN = 36
    IMAGE_HEIGHT = 20
    IMAGE_WIDTH = 59
    # a = name2label('AE86')
    # print(a)
    batch_size =128
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
    a = np.zeros([2, 1])
    print(batch_x)
    print(a)
