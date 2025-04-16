def quadrados_perfeitos(lista):
    quadrados = []
    for i in lista:
        for y in range(1, i+1):
            if y * y == i:
                quadrados.append(i)
    return quadrados
lista = [2, 3, 5, 7,11]
print(quadrados_perfeitos(lista))