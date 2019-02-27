import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.sin(x*np.pi)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.ion()
for i in range(10):
    if i%2==0:
        try:
            ax.lines.remove(lines[0])
        except Exception as e:
            print(e)
        lines = ax.plot(x, y/i, 'r-', lw=5)
        plt.pause(0.3)
        print('x,y=({},{})'.format(x[i], y[i]))


plt.ioff()
plt.show()
