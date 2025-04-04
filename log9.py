frutas = ['Maçã', 'Banana', 'Cereja', 'Manga']
precos = [2.5, 1.2, 3.0, 4.5]

print([frutas[i] + (f': {str(precos[i])}') for i in range(0, len(frutas)) ])