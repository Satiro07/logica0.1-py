numero = int(input('Número: '))
soma = 1
if numero < 0:
    print(f'O número tem que ser maior ou igual a 0!')
else:
    for i in range(numero, 1, -1):
        soma *= i
    print(f'Fatorial de {numero}: {soma}')