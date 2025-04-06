#compreensão de lista
lista1 = []
while True:
    lista = int(input('Digite um número: '))
    if lista == 0:
        break
    if lista not in lista1:
        lista1.append(lista)

print([n**2 for n in range(1, max(lista1)+1) if n**2 in lista1])
