import os

# 主要用于去除txt文本每行最后的换行符，最后一行又没有换行符。
def load_txt(lines):
    for i, item in enumerate(lines):
        if item[-1] == '\n':
            lines[i] = item[0:-1]
    return lines


def show_path():
    print(os.getcwd())
    print(os.get_exec_path())
    print(os.path.dirname(os.path.abspath(__file__)))   # 当前文件的路径


def find_file():
    open()


if __name__ == '__main__':
    show_path()
