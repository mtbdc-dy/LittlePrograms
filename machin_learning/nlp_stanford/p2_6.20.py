# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 8:39 PM
# @Author  : 徐缘
# @File    : p2_6.20.py
# @Software: PyCharm


import nltk                                 # Natural Language Toolkit
from nltk.corpus import wordnet as wn       # 从语料库导入单词网络
# nltk.download()                           # 没有wordnet的话需要下载

panda = wn.synset('panda.n.01')             # synonym sets
hyper = lambda s: s.hypernyms()             # 取变量的上义词

'''
在计算机科学中，闭包又称词法闭包或函数闭包，是引用了自由变量的函数。
这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
闭包被广泛应用于函数式语言中
'''
print(list(panda.closure(hyper)))

poses = {'n': 'noun', 'v': 'verb', 's': 'adj(s)', 'a': 'adj', 'r': 'adv'}
for synset in wn.synsets('good'):
    print("{}: {}".format(poses[synset.pos()],
                          ", ".join([l.name() for l in synset.lemmas()])))




