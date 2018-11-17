# -*- coding: utf-8 -*-
import numpy as np      # 矩阵运算
import cv2  # Open Source Computer Vision Library 计算机视觉
import os   # operation system
import random
import time
from PIL import Image
import random
from os.path import join, exists
import pickle
from sklearn.model_selection import train_test_split
import tensorflow as tf
import math
import argparse
"""
这应该还不能用
就是验证码识别拉 in Tensorflow
"""

# Constants
VOCAB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)
DATA_PATH = 'data'
FLAGS = None

# Functions
def text2vec(text):
    """
   text to one-hot vector
   :param text: source text
   :return: np array
   """
    if len(text) > CAPTCHA_LENGTH:
        return False
    vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
    for i, c in enumerate(text):
        index = i * VOCAB_LENGTH + VOCAB.index(c)
        vector[index] = 1
    return vector


def vec2text(vector):
    """
   vector to captcha text
   :param vector: np array
   :return: text
   """
    if not isinstance(vector, np.ndarray):  # 判断对象是否是一个已知的类型
        vector = np.asarray(vector)         # 如果不是的话转换成 ndarray 注意numpy里有两种数据类型，ndarray和matrix，一
        # 般用ndarray，要用到矩阵的乘除法时再用matrix
    vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])   # 改变数组形状 -1： 自动适配
    text = ''
    for item in vector:
        text += VOCAB[int(np.argmax(item))]    # Returns the indices of the maximum values along an axis.
    return text


def convert_img_into_array():
    """
        convert .img file into numpy arrays
    """

    '''Constant'''
    dir_path = 'trainImage/'

    for path in os.listdir(dir_path):   # listdir 展示目录下的所有文件名
        im = Image.open(dir_path + path)
        im.show()
        captcha_array = np.array(im)
        print(captcha_array)
        print(captcha_array.shape)
        return captcha_array


def generate_data():
    print('Generating Data...')
    data_x, data_y = [], []
    # generate data x and y

    dir_path = 'trainImage/'

    for path in os.listdir(dir_path):   # listdir 展示目录下的所有文件名
        im = Image.open(dir_path + path)
        captcha_array = np.array(im)
        text = path.split('.')[0]
        vector = text2vec(text)
        data_x.append(captcha_array)
        data_y.append(vector)
        # write data to pickle
        if not exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        x = np.asarray(data_x, np.float32)
        y = np.asarray(data_y, np.float32)
        with open(join(DATA_PATH, 'data.pkl'), 'wb') as f:
            pickle.dump(x, f)
            pickle.dump(y, f)


# 归一化
def standardize(x):
    return (x - x.mean()) / x.std()


def generate_dataset():
    with open('data/data.pkl', 'rb') as f:
        data_x = standardize(pickle.load(f))
        data_y = pickle.load(f)
    train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.4, random_state=40)
    dev_x, test_x, dev_y, test_y, = train_test_split(test_x, test_y, test_size=0.5, random_state=40)

    # train and dev dataset
    train_dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y)).shuffle(10000)
    train_dataset = train_dataset.batch(FLAGS.train_batch_size)
    dev_dataset = tf.data.Dataset.from_tensor_slices((dev_x, dev_y))
    dev_dataset = dev_dataset.batch(FLAGS.dev_batch_size)
    test_dataset = tf.data.Dataset.from_tensor_slices((test_x, test_y))
    test_dataset = test_dataset.batch(FLAGS.test_batch_size)

    return train_x, train_y, dev_x, dev_y, test_x, test_y


def main():
    train_x, train_y, dev_x, dev_y, test_x, test_y = generate_dataset()
    train_steps = math.ceil(train_x.shape[0] / FLAGS.train_batch_size)
    dev_steps = math.ceil(dev_x.shape[0] / FLAGS.dev_batch_size)
    test_steps = math.ceil(test_x.shape[0] / FLAGS.test_batch_size)

    global_step = tf.Variable(-1, trainable=False, name='global_step')

    # train and dev dataset
    train_dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y)).shuffle(10000)
    train_dataset = train_dataset.batch(FLAGS.train_batch_size)

    dev_dataset = tf.data.Dataset.from_tensor_slices((dev_x, dev_y))
    dev_dataset = dev_dataset.batch(FLAGS.dev_batch_size)

    test_dataset = tf.data.Dataset.from_tensor_slices((test_x, test_y))
    test_dataset = test_dataset.batch(FLAGS.test_batch_size)

    # a reinitializable iterator
    iterator = tf.data.Iterator.from_structure(train_dataset.output_types, train_dataset.output_shapes)

    train_initializer = iterator.make_initializer(train_dataset)
    dev_initializer = iterator.make_initializer(dev_dataset)
    test_initializer = iterator.make_initializer(test_dataset)

    # input Layer
    with tf.variable_scope('inputs'):
        # x.shape = [-1, 60, 160, 3]
        x, y_label = iterator.get_next()

    keep_prob = tf.placeholder(tf.float32, [])

    y = tf.cast(x, tf.float32)

    # 3 CNN layers
    for _ in range(3):
        y = tf.layers.conv2d(y, filters=32, kernel_size=3, padding='same', activation=tf.nn.relu)
        y = tf.layers.max_pooling2d(y, pool_size=2, strides=2, padding='same')
        # y = tf.layers.dropout(y, rate=keep_prob)

    # 2 dense layers
    y = tf.layers.flatten(y)
    y = tf.layers.dense(y, 1024, activation=tf.nn.relu)
    y = tf.layers.dropout(y, rate=keep_prob)
    y = tf.layers.dense(y, VOCAB_LENGTH)

    y_reshape = tf.reshape(y, [-1, VOCAB_LENGTH])
    y_label_reshape = tf.reshape(y_label, [-1, VOCAB_LENGTH])

    # loss
    cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=y_reshape, labels=y_label_reshape))

    # accuracy
    max_index_predict = tf.argmax(y_reshape, axis=-1)
    max_index_label = tf.argmax(y_label_reshape, axis=-1)
    correct_predict = tf.equal(max_index_predict, max_index_label)
    accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))

    # train
    train_op = tf.train.RMSPropOptimizer(FLAGS.learning_rate).minimize(cross_entropy, global_step=global_step)

    # saver
    saver = tf.train.Saver()

    # iterator
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    # global step
    gstep = 0

    # checkpoint dir
    if not exists(FLAGS.checkpoint_dir):
        os.makedirs(FLAGS.checkpoint_dir)

    if FLAGS.train:
        for epoch in range(FLAGS.epoch_num):
            tf.train.global_step(sess, global_step_tensor=global_step)
            # train
            sess.run(train_initializer)
            for step in range(int(train_steps)):
                loss, acc, gstep, _ = sess.run([cross_entropy, accuracy, global_step, train_op],
                                               feed_dict={keep_prob: FLAGS.keep_prob})
                # print log
                if step % FLAGS.steps_per_print == 0:
                    print('Global Step', gstep, 'Step', step, 'Train Loss', loss, 'Accuracy', acc)

            if epoch % FLAGS.epochs_per_dev == 0:
                # dev
                sess.run(dev_initializer)
                for step in range(int(dev_steps)):
                    if step % FLAGS.steps_per_print == 0:
                        print('Dev Accuracy', sess.run(accuracy, feed_dict={keep_prob: 1}), 'Step', step)

            # save model
            if epoch % FLAGS.epochs_per_save == 0:
                saver.save(sess, FLAGS.checkpoint_dir, global_step=gstep)

    else:
        # load model
        ckpt = tf.train.get_checkpoint_state('ckpt')
        if ckpt:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print('Restore from', ckpt.model_checkpoint_path)
            sess.run(test_initializer)
            for step in range(int(test_steps)):
                if step % FLAGS.steps_per_print == 0:
                    print('Test Accuracy', sess.run(accuracy, feed_dict={keep_prob: 1}), 'Step', step)
        else:
            print('No Model Found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Captcha')
    parser.add_argument('--train_batch_size', help='train batch size', default=128)
    parser.add_argument('--dev_batch_size', help='dev batch size', default=256)
    parser.add_argument('--test_batch_size', help='test batch size', default=256)
    parser.add_argument('--source_data', help='source size', default='./data/data.pkl')
    parser.add_argument('--num_layer', help='num of layer', default=2, type=int)
    parser.add_argument('--num_units', help='num of units', default=64, type=int)
    parser.add_argument('--time_step', help='time steps', default=32, type=int)
    parser.add_argument('--embedding_size', help='time steps', default=64, type=int)
    parser.add_argument('--category_num', help='category num', default=5, type=int)
    parser.add_argument('--learning_rate', help='learning rate', default=0.001, type=float)
    parser.add_argument('--epoch_num', help='num of epoch', default=10000, type=int)
    parser.add_argument('--epochs_per_test', help='epochs per test', default=100, type=int)
    parser.add_argument('--epochs_per_dev', help='epochs per dev', default=2, type=int)
    parser.add_argument('--epochs_per_save', help='epochs per save', default=10, type=int)
    parser.add_argument('--steps_per_print', help='steps per print', default=2, type=int)
    parser.add_argument('--steps_per_summary', help='steps per summary', default=100, type=int)
    parser.add_argument('--keep_prob', help='train keep prob dropout', default=0.5, type=float)
    parser.add_argument('--checkpoint_dir', help='checkpoint dir', default='ckpt/model.ckpt', type=str)
    parser.add_argument('--summaries_dir', help='summaries dir', default='summaries/', type=str)
    parser.add_argument('--train', help='train', default=1, type=int)
    FLAGS, args = parser.parse_known_args()
    main()
