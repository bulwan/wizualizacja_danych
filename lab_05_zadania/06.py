class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

slowo = Wspak("karol")
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))
print(next(slowo))

slowa = Wspak(["madzia", "aneta", "marlenka"])
print(next(slowa))
print(next(slowa))
print(next(slowa))



