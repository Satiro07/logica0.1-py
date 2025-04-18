vetor = [8, 6, 7, 5, 3, 0 ,9]
c = 0
for i in range(0, len(vetor)):
    lei = len(vetor) - c
    minimo = min(vetor[0:lei])
    vetor.append(minimo)
    vetor.remove(minimo)
    c += 1
print(vetor)