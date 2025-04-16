def verificador_senha(senha):
    letra_maiuscula = 0
    letra_minuscula = 0
    espaço = 0
    numero = 0
    if len(senha) >= 8:
        for i in senha:
            if i == i.lower():
                letra_minuscula += 1 
            if ' ' in senha:
                espaço += 1
            if i in '1234567890':
                numero += 1
            else:
                if i == i.upper():
                    letra_maiuscula += 1  
    if letra_maiuscula == 0 or letra_minuscula == 0 or espaço >= 1 or numero == 0:
        return 'Senha inválida'
    else:
        return 'Senha válida'
senha = 'Senha1'
print(verificador_senha(senha))

