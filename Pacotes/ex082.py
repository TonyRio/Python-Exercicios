lista = []
par = []
impar =[]
while True:
    n=(int(input('Digite um número :')))
    lista.append(n)
    if (n%2)==0:
        par.append(n)
    else:
        impar.append(n)
    loop=str(input('Quer continuar ? S/N ')).strip().upper()[0]
    if loop in 'nN':
        break
print(f'\033[34ma lista digitada foi {sorted(lista)}')
print(f'\033[33mos numeros Pares são : {sorted(par)}')
print(f'\033[36mos numeros impares são :{sorted(impar)}')
