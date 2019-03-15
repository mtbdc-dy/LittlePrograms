import myPackages.process_txt as pt

"""
曾几何时，我看我自己写的代码都感觉有点高级了。竟没有一行注释...
不能有冒号哦
而且这个脚本是针对firefox的开发者工具
"""
mode = 1  # 1 for pc. 0 for mac

if mode == 0:
    filename = 'json_dict.txt'
    f = open(filename, 'r', encoding='utf_8')
    lines = pt.load_txt(f.readlines())

    form = dict()
    for item in lines:
        # print(item)
        form[item[0:item.find(':')]] = item[item.find(':')+1:]

    print(form)
else:
    filename = 'json_dict.txt'
    f = open(filename, 'r', encoding='utf_8')
    lines = pt.load_txt(f.readlines())

    print('{')
    for item in lines:
        if '\t' in item:
            # print(item.split('\t'))
            a = item.split('\t')
            print('\'' + a[0] + '\': ', end='')
            if len(a) == 1:
                print('\'\',')
            elif a[1] == '':
                print('\'\',')
            else:
                print('\'' + a[1] + '\',')
        else:
            a = item.split(' ')
            print('\'' + a[0] + '\': ', end='')
            if len(a) == 1:
                print('\'\',')
            elif a[1] == '':
                print('\'\',')
            else:
                print('\'' + a[1] + '\',')

    print('}')




