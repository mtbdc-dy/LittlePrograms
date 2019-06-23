# -*- coding: utf-8 -*-
# @Time : 2019-06-20 21:57
# @Author : 徐缘
# @FileName: sentences_to_vectors.py
# @Software: PyCharm


import csv
import math
from multiprocessing import Process


num_of_process = 7     # 8个还有点勉强，风扇刷刷响。7个明显快了很多     sony 2个也是轻松能稳住的 ^_^


def run_process(r, file):
    import myPackages.bert.bert_sentence_vector as mb
    ret = mb.list_to_vectors(r, 34)
    g = open('output/'+file+'.csv', 'w')
    writer = csv.writer(g)
    for item in ret:
        writer.writerow(item)
    return


filename = 'title.csv'
f = open(filename, 'r')
reader = list(csv.reader(f))

length = len(reader)
n = num_of_process
split_reader = list()
for i in range(n):
    split_reader.append(reader[math.floor(i / n * length):math.floor((i + 1) / n * length)])


for i in range(num_of_process):
    p = Process(target=run_process, args=(split_reader[i], 'vector_'+str(i),))
    p.start()

