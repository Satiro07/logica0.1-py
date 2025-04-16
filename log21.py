def quadrados_perfeitos(lista):
    quadrados = []
    for i in lista:
        for y in i:
            if y * y == i:
                quadrados.append(i)
    return quadrados
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quadrados_perfeitos(lista))