import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)     # Return evenly spaced numbers over a specified interval.
y = np.sin(x*np.pi)             # y = sin(pi x)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)   # 用于一张图显示多张图表，表示共一行，共一列，第一张图
plt.ion()   # 打开交互模式
for i in range(10):
    if i % 2 == 0:              # 0 2 4 6 8 10
        try:
            ax.lines.remove(lines[0])
        except Exception as e:
            print(e)
        lines = ax.plot(x, y/i, 'r-', lw=50)     # red line r+ 红色的×; lw: line width
        plt.pause(0.3)
        print('x,y=({},{})'.format(x[i], y[i]))


plt.ioff()
# plt.show()
