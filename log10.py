#recursão
def fatorial(soma, num):
    soma *= num
    num -=1
    if num != 0:
        return fatorial(soma, num)
    return soma
num = int(input('Digite um número: '))
soma = 1
print(f'Fatorial de {num}: {fatorial(soma, num)}')