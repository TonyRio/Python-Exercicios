lista=[]
while True:
    n=int(input('digite um numero :'))
    lista.append(n)

    loop = str(input('Quer continuar ? S/N :').strip().upper()[0])
    if  loop in 'nN':
            break
print('\033[32m-=-\033[m'*15)
print(f'os numeros digitados foram : {lista}')
print(f'a lista tem {len(lista)} componentes')
print(f'a ordem crescente é : {lista}')
lista.sort(reverse=True)
print(f'a Lista reversa é : {lista}')
if 5 in lista:
    print('\033[34mO valor 5 está na lista')
else:
    print('\033[31mO valor 5 não está na lista')

