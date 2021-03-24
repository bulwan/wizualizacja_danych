plik = open("plik.txt", "w")
for x in range(0, 20, 4):
    x = str(x) + " "
    plik.write(x)
plik.close()
