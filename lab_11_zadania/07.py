import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680801 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.gca(projection = '3d')

n = 20

for c, m, zlow, zhigh in [('r', 'o', 22, 25)]:
    xs = randrange(n, -10, 10)
    ys = randrange(n, -10, 10)
    zs = randrange(n, zlow, zhigh)
    plt.scatter(xs, ys, zs, c=c, marker=m)

t = np.linspace(0 , 15, 15)
x = np.sin(t)
y = t
ax.plot(x, y, zs=0, color='g')

plt.show()