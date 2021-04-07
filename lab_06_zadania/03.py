import numpy as np
def macierz(n):
    return (np.arange(1, n*n+1).reshape(n, n))

n = int(input("Podaj rozmiar macierzy: "))
print(macierz(n))

