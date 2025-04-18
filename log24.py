matriz = [[3, 5, 7], [2, 4, 6], [1, 8, 9]]

for i in matriz:
    print(i)
soma = 0
cont = 0
for i in range(0, len(matriz)):
    soma += matriz[i][cont]
    cont += 1
print(soma)