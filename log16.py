def frequencia_caracteres(palavra):
    dic = {}
    for i in palavra:
        dic[i] = palavra.count(i)
    return dic

palavra = 'banana'
print(frequencia_caracteres(palavra))