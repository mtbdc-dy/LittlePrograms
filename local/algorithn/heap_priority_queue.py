import heapq

"""heapq 函数大全"""
# 建堆
A = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]
pq = [(row[0], i, 0) for i, row in enumerate(A)]
"""Transform list into a heap, in-place, in O(len(x)) time."""
heapq.heapify(pq)   # 直接修改原list





"""无穷大"""
ans = -1e9, 1e9
print(ans)
a = float('inf')
b = float('-inf')
if a > 100000000000:
    print(a)
