import numpy as np
def generuj(podstawa, ilosc):
    m = np.logspace(1, ile, num=ile, base=podstawa, dtype=int)
    return m

podstawa = int(input("Podaj podstawe: "))
ile = int(input("Podaj ile: "))
print(generuj(podstawa, ile))
