dicionario = {}
add_pessoas = int(input('Quantas pessoas irá adicionar? '))
for i in range(0, add_pessoas):
    nome = input('Nome: ')
    dicionario[nome] = int(input('Idade: '))
cont = 1
nome_maior = ''
idade_maior = 0
for k, v in dicionario.items():
    print(f'Pessoa {cont}: {k}, {v} anos')
    if v > idade_maior:
        nome_maior = k
        idade_maior = v
    cont += 1
print(f'A pessoa mais velha é {nome_maior}, com {idade_maior} anos.')
