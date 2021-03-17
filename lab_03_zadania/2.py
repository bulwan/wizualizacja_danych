A = [[0]*4 for i in range(4)]
import random
for x in range(4):
    for z in range(4):
        A[x][z] = [random.randint(0, 10)]
print(A)

lista2=[A[i][i] for i in range(0,4)]
print(lista2)