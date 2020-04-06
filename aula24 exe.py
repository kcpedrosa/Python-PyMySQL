#uso do modulo e resto de divisao
cont = 0
for c in range(1000,2001):
    if c % 11==5:
        print(c)
        cont += 1
print(f'Foram {cont} numeros')

