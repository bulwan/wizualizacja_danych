class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return self.nazwa_produktu + " " + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed

produkt = NaZakupy("chleb",5, "sztuki", 2)
print(produkt.wyswietl_produkt())
print(produkt.ile_produktu())
print(produkt.ile_kosztuje())