# soma pares
lista = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
for numero in pares:
    print(f'{numero}',end=' ')
    if numero == pares[-1]:
        print('=',end=' ')
        break
    print('+',end=' ')
print(sum(pares))