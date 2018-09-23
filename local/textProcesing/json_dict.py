import myPackages.process_txt as pt

filename = 'json_dict.txt'

f = open(filename, 'r')
lines = pt.load_txt(f.readlines())

form = dict()
for item in lines:
    # print(item)
    form[item[0:item.find(':')]] = item[item.find(':')+1:]

print(form)

