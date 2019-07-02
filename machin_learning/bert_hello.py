import tensorflow as tf
from myPackages.bert import modeling
import collections
import os
import numpy as np
import json
import csv
import matplotlib.pyplot as plt                 # 加载matplotlib用于数据的可视化
from sklearn.decomposition import PCA           # 加载PCA算法包


"""
输入一个句子会返回一个句向量。那我的下游任务怎么弄。首先肯定得是有监督的模型。

词向量用的是ELMo（embedding from language models）部分, 双向LSTM，就是蛮奇怪的。

"""


bert_path = '/Users/ShayXU/Downloads/chinese_L-12_H-768_A-12/'

# 显示用了Tensorflow的flags不知道是啥，然后应该是将Google训练好的参数配进去
flags = tf.flags
FLAGS = flags.FLAGS
flags.DEFINE_string(
    'bert_config_file', os.path.join(bert_path, 'bert_config.json'),
    'config json file corresponding to the pre-trained BERT model.'
)
flags.DEFINE_string(
    'bert_vocab_file', os.path.join(bert_path, 'vocab.txt'),
    'the config vocab file',
)
flags.DEFINE_string(
    'init_checkpoint', os.path.join(bert_path, 'bert_model.ckpt'),
    'from a pre-trained BERT get an initial checkpoint',
)
flags.DEFINE_bool("use_tpu", False, "Whether to use TPU or GPU/CPU.")


# 把text转换成Unicode
def convert2Uni(text):
    if isinstance(text, str):
        return text
    elif isinstance(text, bytes):
        return text.decode('utf-8', 'ignore')
    else:
        print(type(text))
        print('####################wrong################')


def load_vocab(vocab_file):
    vocab = collections.OrderedDict()       # 有序字典 可以了解一下
    vocab.setdefault('blank', 2)            # 和get()一起也可以了解一下
    index = 0
    # with tf.gfile.GFile(vocab_file, 'r') as reader:
    with open(vocab_file) as reader:
        while True:
            tmp = reader.readline()
            if not tmp:
                break
            token = convert2Uni(tmp)
            token = token.strip()
            vocab[token] = index            # 字典的value是词向量的顺序？
            index += 1
    print(vocab)                            # 加上一些标点也才21127个。2万个词而已吗?查不到咋整。
    return vocab


# 用向量生成3个输入
# input = vector + [0, 0, 0...]
# mask = [1,...] + [0, 0, 0...] 应为不用训练所以直接把MASK设为全1
# segment = [0, 0, 0, 0, 0....]
def inputs(vectors, maxlen=50):     # 设定句子最长为50-2=48个字
    length = len(vectors)
    if length > maxlen:
        return vectors[0:maxlen], [1]*maxlen, [0]*maxlen
    else:
        input = vectors+[0]*(maxlen-length)
        mask = [1]*length + [0]*(maxlen-length)
        segment = [0]*maxlen
        return input, mask, segment


def response_request(text):
    # 传入一个str吧 生成向量[101, WORDS, 102]
    # [CLS, WORDS, SEP]
    vectors = [dictionary.get('[CLS]')] + [dictionary.get(i) if i in dictionary else dictionary.get('[UNK]') for i in
                                           list(text)] + [dictionary.get('[SEP]')]

    input, mask, segment = inputs(vectors)

    input_ids = np.reshape(np.array(input), [1, -1])    # 1 x N
    input_mask = np.reshape(np.array(mask), [1, -1])
    segment_ids = np.reshape(np.array(segment), [1, -1])

    embedding = tf.squeeze(model.get_sequence_output())     # 去除只有1行的维
    rst = sess.run(embedding, feed_dict={'input_ids_p:0': input_ids, 'input_mask_p:0': input_mask,
                                         'segment_ids_p:0': segment_ids})

    # 好好的列表为什么要转成字符串
    return json.dumps(rst.tolist(), ensure_ascii=False)     # """Serialize ``obj`` to a JSON formatted ``str``.
    # """Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    #     ``.write()``-supporting file-like object).


print('FLAGS.bert_vocab_file:', FLAGS.bert_vocab_file)
dictionary = load_vocab(FLAGS.bert_vocab_file)  # 加载Vocabulary
init_checkpoint = FLAGS.init_checkpoint     # 读取预训练的参数

sess = tf.Session()
bert_config = modeling.BertConfig.from_json_file(FLAGS.bert_config_file)    # 模型配置？

input_ids_p = tf.placeholder(shape=[None, None], dtype=tf.int32, name='input_ids_p')
input_mask_p = tf.placeholder(shape=[None, None], dtype=tf.int32, name='input_mask_p')
segment_ids_p = tf.placeholder(shape=[None, None], dtype=tf.int32, name='segment_ids_p')

model = modeling.BertModel(
    config=bert_config,
    is_training=FLAGS.use_tpu,
    input_ids=input_ids_p,
    input_mask=input_mask_p,
    token_type_ids=segment_ids_p,
    use_one_hot_embeddings=FLAGS.use_tpu,
)
print('####################################')
restore_saver = tf.train.Saver()
restore_saver.restore(sess, init_checkpoint)    # 加载预训练的参数

a = response_request('我叫徐缘。')      # 从
exit()
b = json.loads(a)
# print(b)    # [[x, x, x]]
# print(b[0])
# print(len(b[0]))    # 768 / 3 = 256


# 最重要的是，将文本输入然后将输出保存。
filename = 'title.csv'
f = open(filename, 'r')
reader = csv.reader(f)
x = list()

for i, item in enumerate(reader):
    print(i, ':')
    a = response_request(item)
    b = json.loads(a)
    x.append(b)

pca = PCA(n_components=2)     # 加载PCA算法，设置降维后主成分数目为2
reduced_x = pca.fit_transform(x)    # 对样本进行降维
f.close()

g = open('title_class.csv', 'r')
g_writer = csv.reader(g)
y = list()
class_dict = {
    'ip': 0,
    'cdn': 1,
    'message': 2,
    'wlan': 3,
    'mixed': 4
}
for item in g_writer:
    y.append(class_dict[item])

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
black_x, black_y = [], []
yellow_x, yellow_y = [], []

for i in range(len(reduced_x)):
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])

    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])

    elif y[i] == 2:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

    elif y[i] == 3:
        black_x.append(reduced_x[i][0])
        black_y.append(reduced_x[i][1])

    elif y[i] == 4:
        yellow_x.append(reduced_x[i][0])
        yellow_y.append(reduced_x[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.scatter(black_x, black_x, c='c', marker='x')
plt.scatter(yellow_x, yellow_x, c='m', marker='-')
plt.show()
