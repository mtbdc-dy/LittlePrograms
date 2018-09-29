seen = {2, 2, 3, 4}

print(seen)
MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

A = [1, 2, 3]
# A.reverse()
print(7 << 2)

print(max(range(len(A)), key=lambda item: A[item]))

print(max(i if A[0] else 0 for i in range(10)))

grid = [[5, 2], [3, 4],[6,0]]
a = map(max, grid)
for item in a:
    print(item)
print([sum(i if True else 0 for i in B)for B in [[1,2],[2,3],[4,5]]])

sum(max(grid[i]) for i in range(len(grid))) + len(grid) * len(grid[0]) + sum(max(grid[j][i] for j in range(len(grid))) for i in range(len(grid[0])))