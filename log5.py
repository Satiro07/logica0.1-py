# compreensão de lista
lista1 = []
while True:
    lista = int(input('Digite um número: '))
    if lista == 0:
        break
    if lista not in lista1:
        lista1.append(lista)
print(lista1)
comeco = int(input('começo: '))
comeco1 = comeco
fim = int(input('fim: '))
if comeco > fim:
    comeco = fim
    fim = comeco1
    print(f'Números faltantes : {[n for n in range(comeco, fim+1) if n not in lista1]}')
else:
    print(f'Números faltantes : {[n for n in range(comeco, fim+1) if n not in lista1]}')