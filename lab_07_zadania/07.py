import numpy as np
A = np.arange(6).reshape(2,3)
A = np.sin(A)
B = np.cos(A)
print(A+B)