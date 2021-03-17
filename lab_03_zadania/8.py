def funkcja(a1, r, ile):
    suma = a1
    for x in range(1, ile, 1):
        suma = suma + (a1 + (x*r))
    return suma

print(funkcja(1, 1, 10))

