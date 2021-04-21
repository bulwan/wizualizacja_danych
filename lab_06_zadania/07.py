import numpy as np
def funkcja(n):
    macierz = np.diag([2 for a in range(n)])
    for x in range (1, n):
        pom1 = np.diag([2*(x+1) for _ in range(n-x)], x)
        pom2 = np.diag([2*(x+1) for _ in range(n-x)], -x)
        macierz = macierz + pom1 + pom2
    return macierz

n = input("Podaj n: ")
print(funkcja(int(n)))