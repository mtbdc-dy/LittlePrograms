# 去重算法
nums = [1, 1, 2]

nums_length = len(nums)
index = 0
flag = True    # 为1时，开始去重并计数
for i in range(nums_length):
    if index == 0:  # 第一个数
        value = nums[i]
        index = index + 1
        continue
    if flag:
        if nums[i] == nums[index-1]:
            flag = False
        else:
            nums[index] = nums[i]
            index = index + 1
    elif nums[i] != nums[index-1]:
        flag = True
        nums[index] = nums[i]
        index += 1

print(nums)
print(index-1)
