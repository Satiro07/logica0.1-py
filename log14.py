def recursao(num):
    copia = num
    soma = 0
    while copia:
        num = copia % 10
        copia //= 10
        soma += num
    num = soma
    if num > 10:
        return recursao(num)
    return(num)
num = int(input('Digite um número: '))
print(recursao(num))