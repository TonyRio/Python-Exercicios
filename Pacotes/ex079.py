lista=list()
while True:
    s=int(input('\033[32mdigite um numero :'))
    if s not in lista:
        lista.append(s)
        print('\033[34mvalor adicionado')
    else:
        print('\033[31mnumero ja cadastrado')
    loop=str(input('quer continuar ? S/N :')).strip().upper()[0]
    if loop in 'nN':
        break
print(f'os numeros digitados foram {sorted(lista)} :')

