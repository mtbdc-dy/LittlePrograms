# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 8:39 PM
# @Author  : 徐缘
# @File    : p2_6.20.py
# @Software: PyCharm

import nltk
from nltk.corpus import wordnet as wn

nltk.download()
panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
list(panda.closure(hyper))