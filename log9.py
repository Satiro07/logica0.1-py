frutas = ['Maçã', 'Banana', 'Cereja', 'Manga']
precos = [2.5, 1.2, 3.0, 4.5]

print(frutas[0] + str(precos[0]))

print([frutas+precos for i in enumerate(frutas) if precos])