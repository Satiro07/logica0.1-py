def quadrados_perfeitos(lista):
    quadrados = []
    for i in lista:
        for y in range(1, i+1):
            if y * y == i:
                quadrados.append(i)
    return quadrados
lista = [15, 16, 23, 25, 30, 36]
print(quadrados_perfeitos(lista))