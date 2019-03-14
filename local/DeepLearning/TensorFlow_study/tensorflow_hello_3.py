# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 10:10 PM
# @Author  : 徐缘
# @File    : tensorflow_hello_3.py
# @Software: PyCharm


import tensorflow as tf
from tensorflow import keras

import numpy as np

imdb = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))
