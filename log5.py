lista1 = []
while lista1 != [0]:
    lista = [int(input('Digite um número: '))]
    
    if lista == [0]:
        break
    lista1 += lista
print(lista1)
começo = int(input('Intervalo: '))
fim = int(input())
print([n for n in range(começo, fim+1) if n not in lista1])