def numero_triangular(numero):
    cont = 1
    soma = 0
    while cont <= numero:
        soma += cont
        if soma == numero:
            return True
        elif soma > numero:
            return False
        cont += 1
numero = 10
print(numero_triangular(numero))
