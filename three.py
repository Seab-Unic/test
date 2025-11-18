import random
n=10
m=10
matrix = [[random.randint(10, 100) for t in range(n)] for j in range(m)]
matrix2 = []
for i in matrix:
    matrix2.append(i[-1:1])
for i in matrix:
    for e in i:
        print(e, end='  ')
    print()
