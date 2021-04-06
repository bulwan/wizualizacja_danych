class parzyste:
    x=0
    def __init__(self, imiona):
        self.imiona = imiona
        self.dlugosc = len(imiona)

    def __iter__(self):
        return self

    def __next__(self):
        if self.dlugosc==self.x:
            raise StopIteration
        if self.x%2==0:
            print(self.imiona[self.x])
            self.x = self.x + 1
        else:
            self.x = self.x + 1         

imiona=parzyste(["Jacek","Tomek","Jarek","Kasia","Bartek"])

next(imiona)
next(imiona)
next(imiona)
next(imiona)
next(imiona)



