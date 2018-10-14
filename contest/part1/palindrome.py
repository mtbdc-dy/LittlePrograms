# Longest Palindrome



def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    def preProcess(s):
        if not s:
            return ['^', '$']
        T = ['^']
        for c in s:
            T += ['#', c]
        T += ['#', '$']
        return T

    T = preProcess(s)
    P = [0] * len(T)
    center, right = 0, 0
    for i in range(1, len(T) - 1):
        i_mirror = 2 * center - i
        if right > i:
            P[i] = min(right - i, P[i_mirror])
        else:
            P[i] = 0

        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > right:
            center, right = i, i + P[i]

    max_i = 0
    for i in range(1, len(T) - 1):
        if P[i] > P[max_i]:
            max_i = i
    start = (max_i - 1 - P[max_i]) / 2
    return s[int(start): int(start + P[max_i])]


if __name__ == "__main__":
    filename = 'palindrome' + '.txt'  # 改下文件名
    f = open(filename, 'r')
    reader = f.readlines()

    for item in reader:
        item = item.rstrip()
        # print(item)
        if item[0] == '-':
            continue
        else:
            # print(item)
            print(len(longestPalindrome(item)))

