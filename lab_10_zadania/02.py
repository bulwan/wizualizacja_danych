import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
x = np.linspace(0, 19, 20)
plt.axis([0,20,0,1])
plt.plot(x, 1/x, 'g>:')

plt.xlabel('f(x)')
plt.ylabel('x')
plt.legend()


ax.annotate('inna funkcja', xy=(5, 0.25), xytext=(8, 0.5),
            arrowprops=dict(facecolor='black', shrink=1),
            )
ax.set_ylim(0, 1)

plt.show()