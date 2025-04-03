# usando recursão 0.1
def recursao(num1, num2, soma, cont):
    soma += num1
    cont += 1
    if cont < num2:
        return recursao(num1, num2, soma, cont)
    return (soma)
    
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = 0
cont = 0

print(recursao(num1, num2, soma, cont))
