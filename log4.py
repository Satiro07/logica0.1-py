# usando recursão 0.2
def recursao(num, soma):
    dig = num % 10
    num //= 10
    soma += dig
    if num != 0:
        return recursao(num, soma)
    return(soma)
num = int(input('Digite um número: '))
soma = 0
print(recursao(num, soma))