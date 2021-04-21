import numpy as np
def ciecie(macierz, kierunek):
    pom = macierz.shape
    if kierunek==1:
        pom = int(pom[1])
        if pom%2==1:
            return "nie mozna przeciac macierzy"
        else:
            pom = pom/2
            macierz1 = macierz[0:, 0:int(pom)]
            macierz2 = macierz[0:, int(pom):]
            return ("Macierz 1:\n{} \nMacierz 2:\n{}".format(macierz1, macierz2))
    elif kierunek==2:
        pom = int(pom[0])
        if pom%2==1:
            return "nie mozna przeciac macierzy"
        else:
            pom = pom/2
            macierz1 = macierz[0:int(pom)]
            macierz2 = macierz[int(pom):]
            return ("Macierz 1:\n{} \nMacierz 2:\n{}".format(macierz1, macierz2))

        



macierz = np.array([[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[21,22,23,24,25]])
# kierunek = 1 dla pionowo, 2 dla poziomo
print(ciecie(macierz, 2))