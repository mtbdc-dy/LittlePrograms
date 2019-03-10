# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 2:42 PM
# @Author  : 徐缘
# @File    : tensorflow_hello_2.py
# @Software: PyCharm


"""
Deep Convolutional Generative Adversarial Network(GAN生成式对抗网络)
使用 keras.Sequential模型
epoch 英 /ˈiː.pɒk/   比如训练集有500个样本，batchsize = 10 ，那么训练完整个样本集：iteration=50，epoch=1.
"""


from __future__ import absolute_import, division, print_function
import tensorflow as tf
import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow.keras.layers as layers
import time
from IPython import display


(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
train_images = (train_images - 127.5) / 127.5 # Normalize the images to [-1, 1]

BUFFER_SIZE = 60000
BATCH_SIZE = 256

# Batch and shuffle the data
train_dataset = tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
