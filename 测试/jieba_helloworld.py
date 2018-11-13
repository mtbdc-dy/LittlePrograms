import jieba
from collections import Counter

s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
jieba.load_userdict('jieba_dict.txt')
cut = jieba.cut(s)
print(cut)
print(','.join(cut))
# 我,想,和,女朋友,一起,去,北京故宫博物院,参观,和,闲逛,。

txt = u'欧阳建国是创新办主任也是欢聚时代公司云计算方面的专家'
cut = jieba.cut(txt)
print(','.join(cut))
# 欧阳,建国,是,创新,办,主任,也,是,欢聚,时代,公司,云,计算,方面,的,专家
# 欧阳建国,是,创新办,主任,也,是,欢聚时代,公司,云计算,方面,的,专家
# 欧阳建国,是,创新办,主任,也,是,欢聚时代,公司,云计算,方面,的,专家

def cc():
    # santi_text = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
    santi_text = open('./中文分词.txt', encoding='gbk').read()
    santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 2]
    c = Counter(santi_words).most_common(5)
    print(c[0][0])


if __name__ == '__main__':
    # jieba.load_userdict('user_dict.txt')
    # cc()
    print()
