class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        super().__init__(imie, nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print("Czy jozek jest menadzerem:", (isinstance(jozek, Menadzer)))
print("Czy adrian jest menadzerem:", (isinstance(adrian, Menadzer)))

print("Czy pracownik jest osobą:", (issubclass(Pracownik, Osoba)))
print("Czy pracownik jest menadzerem:", (issubclass(Pracownik, Menadzer)))