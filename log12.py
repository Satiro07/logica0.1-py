def nuns_primo(n):
    primos = []
    for i in range(2, n+1):
        divi = 0
        for y in range(2, n+1):
            if y % i == 0:
                divi += 1
        if divi == 2:
            primos.append(y)
    return primos

numeros = 10
print(nuns_primo(numeros))