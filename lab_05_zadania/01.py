class material:
    def __init__(self):
        self.rodzaj = "bawelna"
        self.dlugosc = "dluga"
        self.szerokosc = "szeroka"

    def wyswietl_nazwe(self):
        return self.rodzaj

class ubrania(material):
    def __init__(self):
        super().__init__()
        self.rozmiar = "XL"
        self.kolor = "czarna"
        self.dla_kogo = "meska"

    def wyswietl_dane(self):
        return 'Rodzaj: {} |  dla kogo: {} |  rozmiar: {} '.format(self.rodzaj, self.dla_kogo, self.rozmiar)

class sweter(ubrania):
    def __init__(self):
        super().__init__()
        self.rodzaj_swetra = "rozpinany"

    def wyswietl_dane(self):
        return 'Sweter: {}'.format(self.rodzaj_swetra)


ubranie = ubrania()
sweterek = sweter()
print(ubranie.wyswietl_dane())
print(sweterek.wyswietl_dane())
print(sweterek.wyswietl_nazwe())