# __ge__ - larger than or equals
# __gt__ - larger than
# __le__ - lower than or equals
# __lt__ - lower than

class zadanie:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __ge__(self, other):
        return self.a >= other.a

    def __gt__(self, other):
        return self.a > other.a

    def __le__(self, other):
        return self.a <= other.a

    def __lt__(self, other):
        return self.a < other.a

cyfra1 = zadanie(5,7)
cyfra2 = zadanie(25,15)

print(cyfra1 > cyfra2)
print(cyfra2 >= cyfra1)
print(cyfra1 < cyfra2)
print(cyfra2 <= cyfra1)
