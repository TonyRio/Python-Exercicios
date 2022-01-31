num = [[],[]]
valor =0
for c in range  (1,8):
    valor= int(input(f'digite {c}.o valor : '))
    if valor%2==0:
         num[0].append(valor)
    else:
        num[1].append(valor)
print('\033[37m|=|-'*15)
print(sorted(num[0]), sorted(num[1]))
print(f'\033[31mos numeros pares são : {sorted(num[0])}')
print(f'\033[34mos numeros impares são {sorted(num[1])}')
