"""
    求出数组中单独出现的数字。其它的都是成对的
"""


def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num      # res = res ^ num
        print(res)
    return res


if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 4, 4]
    print(singleNumber(a))

