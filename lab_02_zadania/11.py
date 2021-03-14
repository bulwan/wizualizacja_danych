wysokosc = input("Podaj liczbe: ")
wysokosc = int(wysokosc)
gwiazdki = 1
gwiazdki = int(gwiazdki)
if wysokosc > 2 and wysokosc < 10:
    if wysokosc%2==0:
        for x in range(int((wysokosc/2)-1), 0, -1):
            print(" "*x + "*"*gwiazdki)
            gwiazdki = gwiazdki + 2
        print("*"*gwiazdki)
        for x in range(0, int(wysokosc/2)+1, 1):
            print(" "*x + "*"*gwiazdki)
            gwiazdki = gwiazdki - 2
    elif wysokosc%2==1:
        for x in range(int((wysokosc/2)), 0, -1):
            print(" "*x + "*"*gwiazdki)
            gwiazdki = gwiazdki + 2
        for x in range(0, int(wysokosc/2)+1, 1):
            print(" "*x + "*"*gwiazdki)
            gwiazdki = gwiazdki - 2