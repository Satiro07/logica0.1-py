def frequencia_caracteres(palavra):
    dic = {}
    for i in palavra:
        dic[i] = palavra.count(i)
    return dic
palavra = 'banana'.lower()
print(frequencia_caracteres(palavra))