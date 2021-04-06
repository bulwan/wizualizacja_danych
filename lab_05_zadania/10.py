import itertools as it

tab = [1,2,3,4,5,6,7,8,9,10]
wynik = list(it.combinations(tab, 3))
# wszystkie wyniki
print(wynik)
# jeden, wybrany wynik
print(wynik[10])