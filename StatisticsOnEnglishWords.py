# 统计一个英文文本中每个单词出现的频率
# 1.读取文本
# 2.提取单词(正交表达)
#

import DocProcess
import re
import operator

file_name = '2016年上海高考英语真题.txt'
file_name_output = 'words list.txt'

lines_count = 0
words_count = 0
chars_count = 0
words_dict = {}
lines_list = []

with open(file_name, 'r') as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count = chars_count + len(line)
        match = re.findall(r'[^a-zA-Z]+', line) # ^ = 否定
        for i in match:
            # 只要英文单词，删掉其他字符
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if len(i) > 2:
                if i.lower() not in words_dict:
                    words_dict[i.lower()] = 1
                else:
                    words_dict[i.lower()] = words_dict[i.lower()] + 1

print('words_count is', len(words_dict))
#print('lines_count is', lines_count)
#print('chars_count is', chars_count)

# for k,v in words_dict.items():
#     print(k,v)
sorted_words_dict = sorted(words_dict.items(),key=operator.itemgetter(1),reverse=1)
for k,v in sorted_words_dict:
    print(k,v)
#print(sorted_words_dict)

with open(file_name_output, 'w') as fo:
    for k,v in sorted_words_dict:
        fo.write(k + ' ' + str(v) + '\n')