import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680801 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111 , projection = '3d')
n = 250

for c, m, zlow, zhigh in [('r', 'o', 22, 25), ( 'orange', '^', 20, 22), ( 'yellow', '>', 17, 20), ( 'green', '*', 15, 17), ( 'blue', '^', 13, 15)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()