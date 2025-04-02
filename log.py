#numero ao contrario
num = int(input('Digite um número: '))
copia_num = num
quantidade_digs = 0
while copia_num:
    copia_num //= 10
    quantidade_digs += 1
inverso = 0
copia_num = num
while quantidade_digs:
    inverso = inverso * 10 + copia_num % 10
    copia_num //= 10
    quantidade_digs -= 1
print(f'Número original -> {num}, número ao contrário -> {inverso}')