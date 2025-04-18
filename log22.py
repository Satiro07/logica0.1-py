vetor = [4, 6, 7, 3, 9]
cont = -1
for i in vetor:
    menor = max(vetor[:cont])
    vetor.remove(menor)
    vetor.append(menor)
    cont -= 1
    i
print(vetor)
        