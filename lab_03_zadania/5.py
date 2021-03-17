
def funkcja(a1, a2):
    if a1==a2:
        return "funkcje sa sobie rownolegle"
    elif a1*a2==(-1):
        return "funkcje sa prostopadle"
    else:
        return "funkcje nie sa ani rownolegle, ani prostopadle"

a1 = int(input("Podaj a pierwszej funkcji: "))
b1 = int(input("Podaj b pierwszej funkcji: "))
a2 = int(input("Podaj a drugiej funkcji: "))
b2 = int(input("Podaj b drugiej funkcji: "))
print(funkcja(a1, a2))
