def numeros_perfeitos(numero):
    quadrados = []
    for i in range(1, numero+1):
        soma = 0
        for y in range(1, i):
            if i % y == 0:
                soma += y
        if soma == i:
            quadrados.append(i)
    return quadrados



numero = 30
print(numeros_perfeitos(numero))