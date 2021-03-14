liczba = input("Podaj liczbe: ")
liczba = int(liczba)
if liczba > 0 and liczba < 11:
    for x in range(1, liczba+1, 1):
        print("A"*x)