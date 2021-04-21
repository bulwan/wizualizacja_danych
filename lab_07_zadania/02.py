import numpy as np
A = np.arange(9).reshape(3,3)
B = np.arange(16).reshape(4,4)

print(A)
print("Minimum macierzy A w poziomie:", np.min(A,axis=0))
print("Minimum macierzy A w pionie:", np.min(A,axis=1))
print(B)
print("Minimum macierzy B w poziomie:", np.min(B,axis=0))
print("Minimum macierzy B w pionie:", np.min(B,axis=1))