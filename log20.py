def sequencia_collatz(numero):
    lista = list()
    lista.append(numero)
    while numero != 1:
        if numero % 2 == 0:
            numero /= 2
            lista.append(numero)
        else:
            numero *=3 +1
            lista.append(numero)
    return lista




numero = 6
print(sequencia_collatz(numero))