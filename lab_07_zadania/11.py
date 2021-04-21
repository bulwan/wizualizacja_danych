import numpy as np
A = np.arange(1, 13)
A = A.ravel()
B = A.reshape(4,3)
B = B.ravel()
C = A.reshape(2,6)
C = C.ravel()

print("MACIERZ A:")
print(A)
print("MACIERZ B:")
print(B)
print("MACIERZ C:")
print(C)