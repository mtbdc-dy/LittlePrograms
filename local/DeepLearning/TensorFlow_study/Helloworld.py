import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # 消除 ‘开启cpu xxx模式'的warning
# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100))  # 随机输入 2 x 100 的 矩阵
# x_data = np.random.rand(100).astype(np.float32)

y_data = np.dot([0.100, 0.200], x_data) + 0.300  # dot 内积 1x2 * 2 x 100 = 1 x 100 一共三百个数据
# 构造一个线性模型
#
b = tf.Variable(tf.zeros([1]))      # Variable() 在 Tensor Flow 里设置变量    1x1的矩阵 也就是只有一个0
#  一个Variable代表一个可修改的张量。，存在在TensorFlow的用于描述交互性操作的图中。它们可以用于计算输入值，也可以在计算中被修改。对于各种机器学习应用，一般都会有模型参数，可以用Variable表示。
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))  # uniform distribution 均匀分布随机取值 1x2 的矩阵 -1 <= x < 1
y = tf.matmul(W, x_data) + b  # Multiplies matrix   tf的变量当然用tf的函数来做运算啦 w(1x2) * x(2 x 100) => 1 x 100

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))  # reduce_mean: reduce dimensions and then calculate mean
optimizer = tf.train.GradientDescentOptimizer(0.5)      # 梯度下降算法
train = optimizer.minimize(loss)        # 用这个算法来最小化方差

# 初始化变量 global_variables_initializer
init = tf.global_variables_initializer()       # 初始化函数的对象。。。自动初始化有问题吗 可能是要重新初始化。毕竟梯度下
# 降是局部最优解。如果不达要求的话，要重新算

# 启动图 (graph)
sess = tf.Session()     # 开启一个 TF 会话
sess.run(init)          # 初始化设定好的变量

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))   # 要run Variable才能取到这个值

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]


# x = tf.placeholder("float", [None, 784])  占位符
