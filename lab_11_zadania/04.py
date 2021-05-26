import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')


_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color='g', alpha=0.3)
ax1.set_title('Wersja 1')

ax2.bar3d(x, y, bottom, width, depth, top, color='r')
ax2.set_title('Wersja 2')

ax3.bar3d(x, y, bottom, width, depth, top, antialiased=False, edgecolor='red', color='pink')
ax3.set_title('Wersja 3')

ax4.bar3d(x, y, bottom, width, depth, top, edgecolor='skyblue', alpha=0.3, color='lightblue', shade=False)
ax4.set_title('Wersja 4')



plt.show()