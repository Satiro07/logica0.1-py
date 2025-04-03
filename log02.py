abc = 'abcdefghijklmnopqrstuvwxyzáéíóúçãõâêîôûàèìòù'
letra_nao = []
frase = input('Digite uma frase: ').lower()
frase.split()
x = ''
cont = 0
for letra in frase:
    x1 = letra
    x += x1
    cont += 1
cont1 = 0
for letra in abc[0:26]:
    if letra not in x:
        letra_nao.append(letra)
    cont += 1
print(letra_nao)