# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 9:35 PM
# @Author  : 徐缘
# @File    : random_tree.py
# @Software: PyCharm


from sklearn import datasets
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

"""
https://scikit-learn.org/stable/modules/ensemble.html
"""


"""1、导入数据"""
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)       # The number of trees in the forest.
clf = clf.fit(X, Y)
print(clf.predict(X))







