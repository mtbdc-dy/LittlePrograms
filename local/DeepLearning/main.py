import argparse
import tensorflow as tf
from os.path import join, exists
from os import makedirs
import pickle
import math
from sklearn.model_selection import train_test_split

# 归一化
def standardize(x):
    return (x - x.mean()) / x.std()


with open('data/data.pkl', 'rb') as f:
    data_x = pickle.load(f)
    data_y = pickle.load(f)


print(standardize(data_x))
print(data_y)
