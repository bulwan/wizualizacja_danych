import numpy as np
A = np.arange(81).reshape(9,9)
print(A)
B = A.reshape(27,3)
print(B)
C = A.reshape(3,27)
print(C)
D = A.reshape(1,81)
print(D)
E = A.reshape(81,1)
print(E)

# rozmar macierzy mozemy zmieniac tylko w taki sposób zeby ilosc wartości wciąż
# była taka sama, wiec z macierzy 9x9 (81 elementów) mozna zrobic
# 3x27, 27x3, 81x1 oraz 1x81