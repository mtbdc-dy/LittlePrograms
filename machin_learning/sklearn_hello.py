# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 11:10 PM
# @Author  : 徐缘
# @File    : sklearn_hello.py
# @Software: PyCharm


from sklearn import datasets
from sklearn import svm
import pickle


"""
https://scikit-learn.org/stable/
"""


"""1、导入数据"""
iris = datasets.load_iris()         # 鸢尾属植物 /ˈaɪrɪs/ 就那个花的数据集
digits = datasets.load_digits()     # 数字

# print(digits.data)      # 用于区分数字的特征
# print(digits.target)    # 标签
print(digits.images[0])
print(len(digits.images))   # 共1797张手写数字灰度图

"""2、拟合和预测"""
# classifier
clf = svm.SVC(gamma=0.001, C=100.)      # support vector classification/machine 支持向量分类/机
# In this example, we set the value of gamma manually. To find good values for these parameters,
# we can use tools such as grid search and cross validation.
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])
print(clf.predict(digits.data[-1:]))

"""3、保存模型"""
s = pickle.dumps(clf)

"""4、读取模型"""
clf2 = pickle.loads(s)
print(clf2.predict(digits.data[-2:]))

