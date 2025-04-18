vetor = [1, 2, 3, 4, 5, 5]
verificação = []
for i in vetor:
    if i not in verificação:
        print(f'{i}: {vetor.count(i)}')
        verificação.append(i)

