
def funkcja(a, b):
    if a>0:
        return "funkcja jest rosnąca"
    elif a<0:
        return "funkcja jest malejaca"
    elif a==0:
        return "funkcja jest stala"

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(funkcja(a,b))
