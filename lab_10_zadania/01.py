import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 20, 100)
plt.axis([0,20,0,1])
plt.plot(x, 1/x, label='funkcja')

ax.annotate('funkcja', xy=(10, 0.15), xytext=(15, 1),
            arrowprops=dict(facecolor='black', shrink=1),
            )
ax.set_ylim(0, 2)

plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend()

plt.show()