lista1 = []
while True:
    lista = int(input('Digite um número: '))
    if lista == 0:
        break
    if lista not in lista1:
        lista1.append(lista)

print([n for n in range(1, len(lista1)+1) if n**2 in lista1])