# -*- coding: utf-8 -*-
import numpy as np      # 矩阵运算
import cv2  # Open Source Computer Vision Library 计算机视觉
import os   # operation system
import random
import time
from PIL import Image


"""
就是验证码识别拉 in Tensorflow
"""

# Constant
VOCAB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)


# Function
def text2vec(text):
    """
   text to one-hot vector
   :param text: source text
   :return: np array
   """
    if len(text) > CAPTCHA_LENGTH:
        return False
    vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
    for i, c in enumerate(text):
        index = i * VOCAB_LENGTH + VOCAB.index(c)
        vector[index] = 1
    return vector


def vec2text(vector):
    """
   vector to captcha text
   :param vector: np array
   :return: text
   """
    if not isinstance(vector, np.ndarray):  # 判断对象是否是一个已知的类型
        vector = np.asarray(vector)         # 如果不是的话转换成 ndarray 注意numpy里有两种数据类型，ndarray和matrix，一
        # 般用ndarray，要用到矩阵的乘除法时再用matrix
    vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])   # 改变数组形状
    text = ''
    for item in vector:
        text += VOCAB[np.argmax(item)]
    return text


if __name__ == '__main__':
    v =

