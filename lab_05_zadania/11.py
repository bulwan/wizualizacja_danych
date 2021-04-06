liczba = int(input("Ile chcesz wygenerowac liczb fibonacciego: "))

def fib(ile):
    mniejsza = 0
    wieksza = 1
    for _ in range(0, ile, 1):
        pomoc = mniejsza
        mniejsza = wieksza
        wieksza = pomoc + wieksza
        yield pomoc
x=fib(liczba)
for a in range (0, liczba):
    print(next(x))