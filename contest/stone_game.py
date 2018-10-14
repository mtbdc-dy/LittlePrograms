import random


def solution(s):
    score = 0
    while len(s) > 1:
        r1 = random.randint(0, len(s)-1)
        r2 = r1
        while r2 == r1:
            r2 = random.randint(0, len(s)-1)
        tmp1 = s[r1]
        tmp2 = s[r2]
        score += tmp1 * tmp2
        s.append(tmp1 + tmp2)
        s.remove(tmp1)   # 删除找到第一个匹配项
        s.remove(tmp2)
        print(s)
    return score


if __name__ == '__main__':

    stones = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]

    print(solution(stones))
