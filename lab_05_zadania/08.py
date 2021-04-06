class samogloski:
    x=0
    def __init__(self, wyraz):
        self.wyraz = wyraz
        self.dlugosc = len(wyraz)

    def __iter__(self):
        return self

    def __next__(self):
        if self.dlugosc==self.x:
            raise StopIteration
        elif self.wyraz[self.x] in "aeoiyuAEOIUY":
            print(self.wyraz[self.x])
            self.x = self.x + 1
        else:
            self.x = self.x + 1

costam = samogloski("rabarbar")
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)
next(costam)



