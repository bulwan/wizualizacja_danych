def generator(data):
    for index in range (0 , len(data)-1, 1):
        if data[index] in "aeoiyuAEOIUY":
            yield data[index]

slowo = generator("Ambulans")
print(next(slowo))
print(next(slowo))
print(next(slowo))



