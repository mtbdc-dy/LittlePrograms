# 游到右下角的最短时间
# heapq

import heapq    # heap queue


def swimInWater(grid):
    N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], {(0, 0)}, 0
    while True:
        T, x, y = heapq.heappop(pq)
        res = max(res, T)
        if x == y == N - 1:
            return res
        for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                seen.add((i, j))
                heapq.heappush(pq, (grid[i][j], i, j))


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)     # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
    return [heapq.heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    li = [[0, 2], [1, 3]]
    print(swimInWater(li))
    print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

    L = [5, 4, 6, 2, 8, 10, 1]
    # 获取列表中最大的三个元素
    print(heapq.nlargest(3, L))
    # 获取列表中最小的三个元素
    print(heapq.nsmallest(3, L))

    info_list = [
        {"name": "laozhang", "age": 20, "score": 90},
        {"name": "laoli", "age": 21, "score": 88},
        {"name": "laowang", "age": 24, "score": 58},
        {"name": "laohe", "age": 22, "score": 77},
        {"name": "laoyang", "age": 21, "score": 89}
    ]

    # 取出年龄最大的两个数据
    print(heapq.nlargest(2, info_list, key=lambda item: item["age"]))

    h = []
    heapq.heappush(h, [4, 2, 3])
    heapq.heappush(h, [1, 2, 3])
    heapq.heappush(h, [2, 1, 3])
    heapq.heappush(h, [3, 2, 3])
    print(h)

    L = [5, 4, 6, 8, 2, 7]
    heapq.heapify(L)
    print(L)


