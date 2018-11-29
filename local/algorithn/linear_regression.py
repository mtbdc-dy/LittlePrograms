import math
import random
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY, MonthLocator
import datetime

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
    return a, b, r


if __name__ == '__main__':



    X = [1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79]
    Y = [242.41,
245.56,
248.18,
251.21,
262.04,
262.76,
259.77,
270.16,
265.3,
273.3,
272.43,
281.16,
278.33,
293.86,
277.28,
282.19,
283.8,
285.84,
293.63,
316.85,
304.73,
298.75,
300.4,
312.62,
330.9,
338.97,
359.94,
354.07,
358.89,
362.19,
365.74,
366.63,
365.76,
368.5,
383.85,
386.85,
381.04,
362.17,
344.65,
395.34,
420.45,
425.24,
425.9,
428.33,
442.53,
443.6,
451.57,
445.18,
440.72,
446.09,
457.91,
462.44,
475.61,
506.09,
493.9,
517.02,
512.4,
539.04,
517.02,
522.72,
523.66,
531.04,
536.83,
535.95,
541.54,
544.72,
560.91,
555.65,
581.64,
566.4,
574.35,
584.38,
573.17,
584.74,
586.85,
602.16,
582.02,
598.44,
601.05]
    Z = list()
    # for item in Y:
    #     Z.append(item)
    # for index in range(80):
    #     a, b, r = linefit(X, Y)
    #     Y.pop(0)
    #     Y.append(round(a * 43 + b, 2))
    #     Z.append(round(a * 43 + b, 2))
        # if tmp % 2 == 0:
        #     Y.append(round(a * 43 + b + r, 2))
        #     Z.append(round(a * 43 + b + r, 2))
        # else:
        #     Y.append(round(a * 43 + b - r, 2))
        #     Z.append(round(a * 43 + b - r, 2))

    a, b, r = linefit(X, Y)
    print(a, b)
    for i in range(100):
        Z.append(round(a * i + b, 2))

    print(len(Z))

    '''date'''

    plt.plot(X, Y, 'ro')
    # plt.axis([0, 6, 0, 20])
    plt.plot(Z)
    plt.ylabel('date rate')
    plt.show()
