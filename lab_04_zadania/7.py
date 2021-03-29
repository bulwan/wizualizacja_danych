class robot:
    def __init__(self, x , y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def gora(self, ile):
        self.y = self.y + (ile*self.krok)

    def dol(self, ile):
        self.y = self.y - (ile*self.krok)

    def lewo(self, ile):
        self.x = self.x - (ile*self.krok)

    def prawo(self, ile):
        self.x = self.x + (ile*self.krok)

    def pokaz_kordy(self):
        return print("x:", self.x, "| y:", self.y)

robocik = robot(10, 5, 1)
robocik.gora(5)
robocik.lewo(10)
robocik.pokaz_kordy()