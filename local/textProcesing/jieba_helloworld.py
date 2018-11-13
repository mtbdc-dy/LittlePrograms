import jieba
from collections import Counter

s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
cut = jieba.cut(s)
print(cut)
print(','.join(cut))


def cc():
    # santi_text = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
    santi_text = open('./中文分词.txt', encoding='gbk').read()
    santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 2]
    c = Counter(santi_words).most_common(5)
    print(c)


if __name__ == '__main__':
    # jieba.load_userdict('user_dict.txt')
    cc()
