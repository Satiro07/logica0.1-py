def frequencia_caracteres(palavra):
    dic = {}
    cont = 0
    for i in palavra:
        dic[i] = palavra.count(i)
    for k in dic.keys():
        cont += 1

    return  cont
palavra = [7,7,7,7,7]
print(frequencia_caracteres(palavra))