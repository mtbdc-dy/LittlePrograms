# max()函数

grid = []
grid.append([1, 2, 3])
print(grid)
n = 1


def a():
    global n
    n = n + 1


print(max(grid[p][q] for p in range(n) for q in range(3)))

