# -*- coding: utf-8 -*-
# @Time : 2019-06-21 00:00
# @Author : 徐缘
# @FileName: visualize_complaints.py
# @Software: PyCharm


import matplotlib.pyplot as plt                 # 加载matplotlib用于数据的可视化
from sklearn.decomposition import PCA           # 加载PCA算法包
from sklearn.datasets import load_iris
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
# exit()

pca = PCA(n_components=2)     # 加载PCA算法，设置降维后主成分数目为2
reduced_x = pca.fit_transform(x)    # 对样本进行降维
# print(reduced_x)
# exit()
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
ip_x, ip_y = [], []
cdn_x, cdn_y = [], []

for i in range(len(reduced_x)):
    if y[i] == 'message':
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])

    elif y[i] == 'wlan':
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])

    elif y[i] == 'ip':
        ip_x.append(reduced_x[i][0])
        ip_y.append(reduced_x[i][1])

    elif y[i] == 'cdn':
        cdn_x.append(reduced_x[i][0])
        cdn_y.append(reduced_x[i][1])

    elif y[i] == 'mixed':
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

# 可视化
plt.scatter(red_x, red_y, c='r', marker='x', label='sms')
plt.scatter(blue_x, blue_y, c='b', marker='D', label='wlan')
plt.scatter(green_x, green_y, c='g', marker='<', label='unknown')
plt.scatter(ip_x, ip_y, c='c', marker='.', label='ip')
plt.scatter(cdn_x, cdn_y, c='gold', marker='4', label='cdn')
plt.legend()
plt.show()
