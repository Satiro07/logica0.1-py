def numeros_perfeitos(numero):
    numeros_perfeitos = []
    for i in range(1, numero+1):
        soma = 0
        for y in range(1, i):
            if i % y == 0:
                soma += y
        if soma == i:
            numeros_perfeitos.append(i)
    return numeros_perfeitos
numero = 497
print(numeros_perfeitos(numero))