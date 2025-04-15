def nuns_primo(n):
    primos = []
    for i in range(2, n+1):
        divi = 0
        for y in range(1, n+1):
            if i % y == 0:
                divi += 1
        if divi == 2:
            primos.append(i)
    return primos

numeros = 10
print(nuns_primo(numeros))