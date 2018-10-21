def pacificAtlantic(matrix):
    PACIFIC, ATLANTIC = 1, 2

    def pacificAtlanticHelper(matrix, x, y, prev_height, prev_val, visited, res):
        if (not 0 <= x < len(matrix)) or \
           (not 0 <= y < len(matrix[0])) or \
           matrix[x][y] < prev_height or \
           (visited[x][y] | prev_val) == visited[x][y]:
            return

        visited[x][y] |= prev_val
        if visited[x][y] == (PACIFIC | ATLANTIC):
            res.append((x, y))

        for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            pacificAtlanticHelper(matrix, x + d[0], y + d[1], matrix[x][y], visited[x][y], visited, res)

    if not matrix:
        return []

    res = []
    m, n = len(matrix),len(matrix[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        pacificAtlanticHelper(matrix, i, 0, float("-inf"), PACIFIC, visited, res)
        pacificAtlanticHelper(matrix, i, n - 1, float("-inf"), ATLANTIC, visited, res)
    for j in range(n):
        pacificAtlanticHelper(matrix, 0, j, float("-inf"), PACIFIC, visited, res)
        pacificAtlanticHelper(matrix, m - 1, j, float("-inf"), ATLANTIC, visited, res)

    return res


if __name__ == '__main__':
    filename = 'water' + '.txt'

    f = open(filename, 'r')  # utf8   gb2312

    reader = f.readlines()

    m = list()
    for item in reader:
        item = item.rstrip()
        row = item.split(' ')
        if item[0] == '-':
            print(len(pacificAtlantic(m)))
            # print(m)
            m = list()
        else:
            n = list()
            for i in row:
                n.append(int(i))
            m.append(n)
