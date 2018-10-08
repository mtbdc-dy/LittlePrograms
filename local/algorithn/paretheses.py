class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        def isEmpty(x):
            if len(x) == 0:
                return True
            else:
                return False

        def peak(x):
            return x[len(x) - 1]

        if isEmpty(S):
            return 0

        l = list()
        for s in S:
            if s == '(':  # 当前值是左括号
                l.append(s)
            else:  # 当前值是右括号
                last = l.pop()
                if last == '(':  # 前面是个左括号
                    if isEmpty(l):
                        l.append(1)
                    else:
                        if peak(l) != '(':
                            l.append(l.pop() + 1)
                        else:
                            l.append(1)
                else:
                    print(l.pop())
                    tmp = last * 2
                    if isEmpty(l):
                        l.append(tmp)
                    else:
                        if peak(l) == '(':
                            l.append(tmp)
                        else:
                            l.append(l.pop() + tmp)

        print(l)
        return l[0]


if __name__ == '__main__':
    a = Solution()
    S = "(()(()))"
    a.scoreOfParentheses(S)

