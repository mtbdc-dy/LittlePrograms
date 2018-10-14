from operator import add, sub, mul, truediv


def judge_point_24(nums):
    if len(nums) == 1:
        return abs(nums[0]-24) < 1e-6
    ops = [add, sub, mul, truediv]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            next_nums = [nums[k] for k in range(len(nums)) if i != k != j]
            for op in ops:
                if ((op is add or op is mul) and j > i) or (op == truediv and nums[j] == 0):
                    continue
                next_nums.append(op(nums[i], nums[j]))
                if judge_point_24(next_nums):
                    return True
                next_nums.pop()
    return False


if __name__ == '__main__':
    filename = 'game' + '.txt'

    f = open(filename, 'r')  # utf8   gb2312

    reader = f.readlines()

    for item in reader:
        item = item.rstrip()
        row = item.split(',')

        n = list()
        for i in row:
            n.append(int(i))

        # n = [1,2,1,2]
        # print(row)
        if judge_point_24(n):
            print('true')
        else:
            print('false')



