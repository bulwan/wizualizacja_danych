with open("plik2.txt", "w+") as plik:
    for x in range(1, 11):
        x = str(x) + " "
        plik.write(x)
plik = open("plik2.txt", "r")
tekst = plik.read()
print(tekst)
