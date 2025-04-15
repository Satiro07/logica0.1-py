# num = int(input('Digite um valor: '))
# copia_num = copia = num
# soma_f = cont =  0
# while True:
#     soma = digs = 0
#     while copia_num:
#         copia_num //= 10  
#         digs += 1
#     if digs == 1:
#         print(num if cont == 0 else soma_f)
#         break
#     for c in range(0, digs):
#         digito = copia % 10
#         soma += digito
#         copia //=10
#     copia_num = copia = soma_f = soma
#     cont += 1

def recursao(num):
    copia = num
    soma = 0
    while copia:
        num = copia % 10
        copia //= 10
        soma += num
    num = soma
    if num > 10:
        return recursao(num)
    return(num)
num = int(input('Digite um número: '))
print(recursao(num))