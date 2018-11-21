import math
import random


def linefit(x, y):
    N = float(len(x))
    sx, sy, sxx, syy, sxy = 0, 0, 0, 0, 0
    for i in range(0, int(N)):
        sx += x[i]
        sy += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    a = (sy*sx/N -sxy)/( sx*sx/N -sxx)
    b = (sy - a*sx)/N
    r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b,r


if __name__ == '__main__':
    # 675
    X = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42, 43]
    Y = [4.57, 4.55, 4.58, 4.74, 4.86, 4.92, 4.88, 4.92, 4.92, 5.1, 5.07, 5.23, 5.24, 5.38, 5.01, 5.03, 5.12, 5.12, 5.36, 5.84, 5.56, 5.53, 5.59, 5.78, 6.09, 6.27, 6.48, 6.35, 6.4, 6.47, 6.38, 6.65, 6.51, 6.58, 6.69, 6.91, 6.9, 7.03, 6.38, 7.27, 7.78, 7.78, 7.88]
    Z = list()
    for item in Y:
        Z.append(item)
    for index in range(80):
        a, b, r = linefit(X, Y)
        Y.pop(0)
        tmp = random.randint(0, 99)
        Y.append(round(a * 43 + b, 2))
        Z.append(round(a * 43 + b, 2))
        # if tmp % 2 == 0:
        #     Y.append(round(a * 43 + b + r, 2))
        #     Z.append(round(a * 43 + b + r, 2))
        # else:
        #     Y.append(round(a * 43 + b - r, 2))
        #     Z.append(round(a * 43 + b - r, 2))

    print(r)
    print(Z)
    print(len(Z))
    # print("X=", X)
    # print("Y=", Y)
    # print("拟合结果: y = %10.5f x + %10.5f , r=%10.5f" % (a,b,r) )
