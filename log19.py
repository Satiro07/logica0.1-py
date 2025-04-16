def frequencia_caracteres(lista):
    dic = {}
    cont = 0
    for i in lista:
        dic[i] = lista.count(i)
    for k in dic.keys():
        cont += 1

    return cont
palavra = [1, 2, 3, 2, 4, 1, 5]
print(frequencia_caracteres(palavra))