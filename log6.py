def recursao(frase, cont, contagem):
    vogal = ['a', 'e', 'i', 'o', 'u', 'á', 'ã', 'â', 'é', 'ê', 'í', 'î', 'ó', 'õ', 'ô', 'ú', 'û']
    if frase[cont] in vogal:
        contagem += 1
    cont += 1
    if len(frase) != cont:
        return recursao(frase, cont, contagem)
    return contagem

frase = input('digite uma frase: ').lower().strip()
cont = 0
contagem = 0
resp = recursao(frase, cont, contagem)
print(f'Quantidade de vogais na frase: {resp}')