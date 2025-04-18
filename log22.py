vetor = [4, 6, 7, 3, 9]
cont = -1
for i in range(0, len(vetor)):
    menor = min(vetor[:cont])
    vetor.remove(menor)
    vetor.append(menor)
    cont -= 1
    if cont == -len(vetor):
        vetor.append(vetor[0])
        vetor.remove(vetor[0])
        break
print(vetor)
        