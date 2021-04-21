import numpy as np
A = np.arange(9).reshape(3,3)
for x in A.flat:
    print(x)
