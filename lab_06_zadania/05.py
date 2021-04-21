import numpy as np
def funkcja(dlugosc):
    return (np.diag(np.arange(dlugosc, 0, -1)))

dlugosc = int(input("Podaj dlugosc: "))
print(funkcja(dlugosc))
