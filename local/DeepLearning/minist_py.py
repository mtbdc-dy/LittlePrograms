from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
batch_xs, batch_ys = mnist.train.next_batch(10)
print(len(batch_xs))
print(type(batch_xs))
print(len(batch_ys))
print(type(batch_ys))
print(batch_ys)
