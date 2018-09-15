import chardet


# 显示文件编码
with open("新建文本文档.txt", "rb") as f:
    data = f.read()
    print(chardet.detect(data))

with open("第一问答案.txt", 'rb') as g:
    data = g.read()
    print(chardet.detect(data))

filename = 'encoding_test.txt'

f = open(filename, 'w')
lines = 'asdasdadasdadad'
f.writelines(lines)
f.close()

with open(filename, 'r') as f:
    print(f.readline())
    print(chardet.detect(data))

