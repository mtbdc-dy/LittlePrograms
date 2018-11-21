"""岛的最大面积"""


class Solution:
    def maxAreaOfIsland(self, grid):
        seen = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) +
                    area(r, c - 1) + area(r, c + 1))

        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))


if __name__ == '__main__':
    list = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    a = Solution()
    m = a.maxAreaOfIsland(list)
    print(m)

