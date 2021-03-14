liczba = input("Podaj liczbe: ")
liczba = int(liczba)
reszta = 0
suma = 0
while (liczba>0.9):
    reszta = liczba%10
    liczba = (liczba-reszta)/10
    suma = suma + reszta
print(suma)