import csv
import codecs


# SLB POLICY 和 Group Method
# POLICY、Group Method 对应 组
# 组里有 很多real ip 和 一个virtual ip 但是他们又有很多接口


input_filename = 'array1运行配置20180712.txt'
output_filename = 'array1配置.csv'
output_filename2 = 'array1配置_组成员.csv'

f = open(input_filename, 'r')
lines = f.readlines()

g = open(output_filename, 'w')
writer = csv.writer(g)

z = open(output_filename2, 'w')
writer2 = csv.writer(z)

group_name = []
real_ip = []

for item in lines:
    var = item.split()
    if len(var) >= 4:
        if var[1] == 'group' and var[2] == 'method':
            group_name.append(var[3])

for name in group_name:
    output = [name]
    member = ''
    flag = True
    for item in lines:
        var = item.split()
        if len(var) >= 3:
            if var[1] == 'policy' and var[2] == 'default' and var[4] == name:
                policy = var[3]
                output.append(policy)
                flag = False

    if flag:
        output.append('')

    for item in lines:
        var = item.split()
        if len(var) >= 3:
            if var[0] == 'slb' and var[1] == 'virtual' and var[2] == 'tcp' and var[3] == policy:
                output.append(var[4])
                output.append(var[5])
            if var[0] == 'slb' and var[1] == 'virtual' and var[2] == 'ip' and var[3] == policy:
                output.append(var[4])
                output.append('')
            # 找组成员
            if var[0] == 'slb' and var[1] == 'group' and var[2] == 'member' and var[3] == name:
                # print(var)
                member = member + var[4] + '\n'
                output_2 = [var[4], name]
                for i in lines:
                    v = i.split()
                    if len(v) >= 9:
                        if v[0] == 'slb' and v[1] == 'real' and v[2] == 'tcp' and v[3] == var[4]:
                            print(v)
                            output_2.append(v[4])
                            output_2.append(v[5])
                        if v[0] == 'slb' and v[1] == 'real' and v[2] == 'ip' and v[3] == var[4]:
                            output_2.append(v[4])
                            output_2.append('')
                writer2.writerow(output_2)

    output.append(member)
    writer.writerow(output)
