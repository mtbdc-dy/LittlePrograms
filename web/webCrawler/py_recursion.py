class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        def cal_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        max_t = 0
        for item in ghosts:
            max_tmp = abs(item[0] - target[0]) + abs(item[1] - target[1])
            if max_tmp > max_t:
                max_t = max_tmp

        def recursion(position, t):
            for item in ghosts:
                if cal_distance(position, item) <= t:
                    return False

            if position == target:
                return True

            for i in [[1, 0], [0, 1]]:
                if 0 <= position[0] + i[0] <= target[0] and 0 <= position[1] + i[1] <= target[1] and t + 1 < max_t:
                    if recursion([position[0] + i[0], position[1] + i[1]], t + 1):
                        return True

            return False

        return recursion([0, 0], 0)


if __name__ == '__main__':
    obj = Solution()
    print(obj.escapeGhosts([[1, 0], [0, 3]], [0, 1]))