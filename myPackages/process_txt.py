# 主要用于去除txt文本每行最后的换行符，最后一行又没有换行符。
def load_txt(lines):
    for i, item in enumerate(lines):
        if item[-1] == '\n':
            lines[i] = item[0:-1]
    return lines
