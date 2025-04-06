numero = int(input('Número: '))
soma = 1
for i in range(numero, 1, -1):
    soma *= i
print(f'Fatorial de {numero}: {soma}')