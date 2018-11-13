import jieba
from collections import Counter


def ct():
    santi_text = open('./eoms_complaints.txt', encoding='gbk').read()
    santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 2]
    c = Counter(santi_words).most_common(500)
    print(c)
    print(len(c))
    return c


if __name__ == '__main__':
    jieba.load_userdict('emos_complaints_jieba_dict.txt')
    count = 0
    li = ct()
    for item in li:
        if str(item[0]).isdigit():
            continue
        if count >= 199:
            break
        print('{')
        print('\tname: \'' + item[0] + '\',')
        print('\tvalue: \'' + str(item[1]) + '\',')
        print('},')
        count += 1
