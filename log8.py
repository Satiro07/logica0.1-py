#compreensão de lista
print('Lista 1')
lista1 = []
while True:
    lista = int(input('Digite um número: [lista 1] '))
    if lista == 0:
        break
    if lista not in lista1:
        lista1.append(lista)
print('Lista 2')
lista2 = []
while True:
    lista = int(input('Digite um número: [lista 2] '))
    if lista == 0:
        break
    if lista not in lista2:
        lista2.append(lista)

print([n for n in lista1 if n in lista2])