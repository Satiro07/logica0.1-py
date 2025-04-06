def remover_negativo(lista, cont):
    if cont < len(lista):
        if lista[cont] < 0:
            lista.remove(lista[cont])
            cont -= 1
        cont += 1
        return remover_negativo(lista, cont)
    return lista
        
lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    continuar = input('deseja continuar? ["s" para sair] ').lower()
    if continuar == 's':
        break
cont = 0
print(f'Lista original: {lista}')
print(f'Nova lista: {remover_negativo(lista, cont)}')