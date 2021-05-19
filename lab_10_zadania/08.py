import numpy as np
import matplotlib.pyplot as plt


def rzuty(n):
    return [(np.random.randint(1,7)+np.random.randint(1,7)) for _ in range(n)]

n = input("podaj liczbe rzutow:")
n = int(n)
wynik = rzuty(n)

plt.hist(wynik, bins=11, facecolor='g')
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.grid(True)
plt.show()
