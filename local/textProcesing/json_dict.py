import myPackages.process_txt as pt

"""IMPORTANT"""
mode = 0  # 1 for pc. 0 for mac

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
        # print(item)
        # print(item.split('\t'))
        a = item.split('\t')
        print('\'' + a[0] + '\': ', end='')
        if a[1] == '':
            print('\'\',')
        else:
            print('\'' + a[1] + '\',')

    print('}')




