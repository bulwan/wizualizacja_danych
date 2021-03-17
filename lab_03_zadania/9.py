def funkcja(a1=1, r=1, ile=10):
    iloczyn = a1
    for x in range(1, ile, 1):
        iloczyn = iloczyn * (a1 + (x*r))
    return iloczyn


a1 = int(input("Podaj a1: "))
r = int(input("Podaj r: "))
ile = int(input("Podaj z ilu elementow chcesz obliczyc iloczyn: "))
print(funkcja(a1, r, ile))

