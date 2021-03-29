class slowa:
    def __init__(self, slowo1, slowo2):
        self.slowo1=slowo1.lower()
        self.slowo2=slowo2.lower()

    def palindrom(self):
        dlugosc = len(self.slowo1)
        x = 1
        while (x<=dlugosc):
            if self.slowo1[x-1]==self.slowo1[(-1)*x]:
                pom = 1
            else:
                pom = 0
            x = x + 1
        if pom == 1:
            return "slowo pierwsze jest palindromem"
        else:
            return "slowo pierwsze nie jest palindromem"

    def metagram(self):
        pomoc = 0
        if len(self.slowo1) != len(self.slowo2):
            return "to nie jest metagram"
        else:
            for x in range(0, len(self.slowo1)):
                if self.slowo1[x] != self.slowo2[x]:
                    pomoc = pomoc + 1
            if pomoc!=1:
                return "to nie jest metagram"
            else:
                return "to jest metagram"

    def anagram(self):
        k = 0
        if len(self.slowo1) != len(self.slowo2):
            return "to nie jest anagram"
        else:
            s1 = list(self.slowo1)
            s2 = list(self.slowo2)
            s1.sort()
            s2.sort()
            if s1 == s2:
                return "to jest anagram"
            else:
                return "to nie jest anagram"
    
    def wyswietl(self):
        print("piersze slowo to: ", self.slowo1)
        print("drugie slowo to: ", self.slowo2, end="")
        return ""
     
    def __del__(self):
        return ""


slowo = slowa("Natan", "natan")
print(slowo.palindrom())
print(slowo.metagram())
print(slowo.anagram())

#sprawdzenie del
print("--s p r a w d z e n i e--")
print(slowo.wyswietl())
del slowo
print(slowo.wyswietl())

