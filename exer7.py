import random

# define tamanho
M = 3
N = 3

# gera as matrizes
matriz1 = [[random.randint(0, 255) for j in range(N)] for i in range(M)]
matriz2 = [[random.randint(0, 255) for j in range(N)] for i in range(M)]

# soma matrizes
result = [[0 for j in range(N)] for i in range(M)]
for i in range(M):
    for j in range(N):
        result[i][j] = matriz1[i][j] + matriz2[i][j]

# mostra resultados tratando under e overflow
underFlow = [[min(result[i][j], 255) for j in range(N)] for i in range(M)]
overFlow = [[result[i][j] % 256 for j in range(N)] for i in range(M)]
both = [[max(result[i][j] -255, 0) for j in range(N)] for i in range(M)]

print("Matriz 1:")
for row in matriz1:
    print(row)

print("Matriz 2:")
for row in matriz2:
    print(row)

print("Resultado:")
for row in result:
    print(row)

print("Resultado com underflow tratado:")
for row in underFlow:
    print(row)

print("Resultado com overflow tratado:")
for row in overFlow:
    print(row)

print("Resultado com underflow e overflow tratados:")
for row in both:
    print(row)