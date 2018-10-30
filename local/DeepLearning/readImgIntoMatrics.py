# -*- coding: utf-8 -*-
import numpy as np      # 矩阵运算
import cv2  # Open Source Computer Vision Library 计算机视觉
import os   # operation system
import random
import time
from PIL import Image


def convert_img_into_array():
    """
        convert .img file into numpy arrays
    """

    '''Constant'''
    dir_path = 'trainImage/'

    for path in os.listdir(dir_path):   # listdir 展示目录下的所有文件名
        im = Image.open(dir_path + path)
        im.show()
        captcha_array = np.array(im)
        print(captcha_array)
        print(captcha_array.shape)
        return captcha_array


if __name__ == '__main__':
    convert_img_into_array()
    print()
