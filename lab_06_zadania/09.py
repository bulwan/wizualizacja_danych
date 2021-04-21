import numpy as np
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

liczby = np.arange(25)
for x in range(0, 25):
        liczby[x] = fibonacci(x)
liczby = liczby.reshape((5,5))

print(liczby)