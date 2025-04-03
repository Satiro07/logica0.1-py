lista1 = []
while True:
    lista = int(input('Digite um número: '))
    if lista == 0:
        break
    if lista not in lista1:
        lista1.append(lista)

print(f'saida: {[i for i in range(1, len(lista1)) if i * i in lista1]}')