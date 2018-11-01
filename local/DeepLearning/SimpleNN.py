# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def loadData(filename):
    df = pd.read_table(filename, '\t', header=None)
    return np.array(df.loc[:, 0:1]), np.array(df.loc[:, 2])

def showData(X, y, w=None, b=None):
    plt.scatter(X[:,0], X[:,1], c=y, edgecolors='k')

    if (w is None) or (b is None):
        pass
    else:
        a = -w[1, 0] / w[0, 0]
        b = -b / w[1, 0]
        plt.plot(X[:, 0], a * X[:, 0] + b, c='red')
    plt.show()

def init_w_b(shape_w, shape_b, seed):
    np.random.seed(seed)
    w = np.random.rand(shape_w[0], shape_w[1])
    b = np.random.rand(shape_b[0]) + 0.01
    return w, b


def forward(X, w, b):
    z = np.dot(X, w) + b
    a = 1.0 / (1.0 + np.exp(-z))
    return a

def cost_func(y_, y):
    y_ = y_.flatten()
    y = y.flatten()
    # cost = np.average( -(y*np.log(y_) + (1-y)*np.log(1-y_)) )
    cost = np.sum(np.power(y_ - y, 2)) / y.shape[0]
    return cost

def train(maxloop, alpha, X, y, w, b):
    m = X.shape[0]
    y = y.reshape((m, 1))
    cost_list = []
    for i in range(maxloop):
        a = forward(X, w, b)
        d_z = a - y
        d_w = np.dot(X.T, d_z) / m
        d_b = np.sum(d_z) / m
        w = w - alpha * d_w
        b = b - alpha * d_b
        y_ = a
        cost = cost_func(y_,y)
        cost_list.append(cost)
        # print(cost_func(y_, y))
        print(calc_accuarcy(y_, y))
    return w, b, cost_list

def harden(y_, sepNum):
    y_[y_ > sepNum] = 1
    y_[y_ <= sepNum] = 0
    return y_

def calc_accuarcy(y_, y):
    y = y.flatten()
    y_ = y_.flatten()
    y_ = harden(y_, 0.5)
    correctNum = len(y_[y_ == y])
    return float(correctNum) / y.shape[0]

def showSatter3D(X,y):
    ax = plt.figure().add_subplot(111, projection = '3d')
    ax.scatter(X[:,0],X[:,1],X[:,2], c=y,  edgecolors='k')  # 点为红色三角形
    # 设置坐标轴
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    # 显示图像
    plt.show()

# ------------ main -------------- #
X, y = loadData('./testSet.txt')
#showData(X, y)
print X
print y

w, b = init_w_b([2, 1], [1], seed=314)
a = forward(X, w, b)
y_ = a.flatten()
cost = cost_func(y_, y)
w, b, cost_list = train(400, 0.1, X, y, w, b) # hidden-layer training

y_ = forward(X, w, b)
y_ = harden(y_, 0.5)
# show cost function value
#plt.plot(cost_list)
#plt.show()

y_=y_.flatten()
print y_
showData(X, y, w, b)
showData(X, y_, w, b)
syn0 = 2*np.random.random((3,1))-1
print syn0


# test 2
# sigmoid_derivative = x*(1-x)

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in xrange(500):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    y_predict = l2.flatten()
    y_predict = harden(y_predict ,0.5)
    l2_error = y - l2
    l2_delta = l2_error*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)


y=y.flatten()
showSatter3D(X,y)
showSatter3D(X,y_predict)

