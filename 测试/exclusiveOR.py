def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
        print(res)
    return res


if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 4, 4]
    print(singleNumber(a))