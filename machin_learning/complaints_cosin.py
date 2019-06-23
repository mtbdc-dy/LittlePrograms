# -*- coding: utf-8 -*-
# @Time : 2019-06-22 00:33
# @Author : 徐缘
# @FileName: complaints_cosin.py
# @Software: PyCharm



import matplotlib.pyplot as plt                 # 加载matplotlib用于数据的可视化
from sklearn.decomposition import PCA           # 加载PCA算法包
from sklearn.metrics.pairwise import cosine_similarity
import csv


filename = 'archive/title_vector_34.csv'
f = open(filename, 'r')
reader = csv.reader(f)

g = open('title_class.csv', 'r')
reader_tiltle = csv.reader(g)

# data = load_iris()
x = [x for x in reader]
y = [x[0] for x in reader_tiltle]
# print(x)
# print(y)
print(cosine_similarity(x).shape)
print(cosine_similarity(x))
