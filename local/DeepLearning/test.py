import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def loadDataSet():
    dataMat  = []
    labelMat = []
    fr = open('./testSet.txt','r')
    lines = fr.readlines()
    for line in lines:
        strArr = line.strip().split()
        dataMat.append([float(strArr[0]),float(strArr[1])])
        labelMat.append(int(strArr[2]))
        # dataMat = np.mat(dataMat)
        # labelMat = np.mat(labelMat).reshape(np.shape(dataMat)[0], 1)
    return np.array(dataMat),np.array(labelMat)

def f_Z(X, w, b):
    Z = np.dot(X, w.T) + b
    return Z

def f_A(Z):     # activation function (sigmoid function)
    A = 1.0 / (1.0 + np.exp(-Z))
    return A

def f_dz(X, y, w, b):     # Error
    Z = f_Z(X, w, b)
    A = f_A(Z)
    dz = A - y
    return dz

def f_dw(X, y, w, b):
    m = np.shape(X)[0]
    dz = f_dz(X, y, w, b)
    dw = np.dot(dz.T, X) / float(m)
    return dw

def f_db(X, y, w, b):
    m = np.shape(X)[0]
    dz = f_dz(X, y, w, b)
    db = np.sum(dz) / float(m)
    return db

def bp(X, y, alpa=0.1):
    cost_list = []
    cost_old = 1
    w = np.array([1, 1])
    b = 1.0
    maxCycle = 500
    eclipse = 0.00005
    for k in range(maxCycle):
        dw = f_dw(X, y, w, b)
        db = f_db(X, y, w, b)
        w = w - alpa * dw
        b = b - alpa * db
        cost = costFunc(X, y, w, b)
        cost_list.append(cost)
        cost_old = cost_list[len(cost_list)-2]
        if k>3 and abs(cost_old-cost) < eclipse:
            break
    return w, b, cost_list

def costFunc(X, y, w, b):
    m = np.shape(X)[0]  # sample number
    Z = f_Z(X, w, b)
    A = f_A(Z)
    diff = A - y
    cost = np.sum(np.power(diff, 2)) / m
    return cost

def showData(X, y):
    plt.scatter(X[:,0], X[:,1], c=y,edgecolor='k')
    plt.show()

def showCost(axis,cost_list):
    plt.plot(axis,cost_list,c='y')
    plt.show()


X, y = loadDataSet()
showData(X, y)


w, b, cost_list = bp(X, y)

a = -w[0] / w[1]
b = -b / w[1]

Z = np.dot(X, w.T) + b
print(Z)

# plot line
plt.scatter(X[:,0], X[:,1], c=y, edgecolor='k')
plt.plot(X[:,0], a*X[:,0]+b, c='r')
plt.show()


print(len(cost_list))
axis = np.arange(1,len(cost_list)+1)
showCost(axis,cost_list)