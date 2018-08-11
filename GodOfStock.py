A = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]


R, C = len(A), len(A[0])
ans = [[None] * R for _ in range(C)]
print(ans)
for r, row in enumerate(A):
    print(r, row)
    for c, val in enumerate(row):
        ans[c][r] = val

# print(ans)
