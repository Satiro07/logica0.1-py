def soma_digitos(num):
    copia = num
    digitos = 0
    soma = 0
    while copia:
        copia //= 10
        digitos += 1
    while digitos:
        soma += num%10
        num //= 10
        digitos -=1
    return soma
numero = 123
print(soma_digitos(numero))
