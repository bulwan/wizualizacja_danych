class Kwadrat:
    def __init__(self, x):
        self.x = x
        self.y = x
    def __add__(self,other):
        self.x = self.x+other.x
        self.y = self.x
        print("nowy x:{} | nowy y:{}".format(self.x, self.y))
        
kw1=Kwadrat(5)
kw2=Kwadrat(3)
kw1+kw2