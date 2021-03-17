def funkcja(a1=1, r=1, ile=10):
    suma = a1
    for x in range(1, ile, 1):
        suma = suma + (a1 + (x*r))
    return suma


a1 = int(input("Podaj a1: "))
r = int(input("Podaj r: "))
ile = int(input("Podaj ile elementow chcesz sumowac: "))
print(funkcja(a1, r, ile))

