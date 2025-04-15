# def palindromo(frase):
#     palavra = ''
#     for i in range(len(frase)-1, -1, -1):
#         palavra += frase[i]
#     return palavra == frase
# f = 'python'
# print(palindromo(f))

def palindromo(frase):
    return frase == frase[::-1]
f = 'ana'
print(palindromo(f))