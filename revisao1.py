def media(soma, quantidade):
    if quantidade == 0:
        return 'adicione uma nota!'
    media = soma / quantidade
    return media
soma_notas = 0
quantidade_notas = 0
while True:
    n1 = int(input('Digite uma nota: ["-1" para sair] '))
    if n1 < 0:
        break
    soma_notas += n1
    quantidade_notas += 1
print(media(soma_notas, quantidade_notas))