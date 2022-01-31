ficha = list()
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1 :'))
    nota2 = float(input('nota 2 :'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [[nota1], [nota2]], media])

    loop = str(input('Quer continuar N/S ?'))
    if loop in 'nN':
        break
print('\033[34m-=' * 30)
print(f'{"No.":^4}{"NOME":^10}{"MÉDIA":^8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'|{i:^4}|{a[0]:^10}|{a[2]:^8.1f}|')
while True:
    print('__' * 30)
    opc = int(input('qual Aluno quer ver as notas ? \033[31m999 para sair\033[m '))
    if opc==999:
        print('\nFINALIZADO\nOBRIGADO POR USAR O SISTEMA.')
        break
    if opc<=len(ficha)-1:
       print(f'as notas do aluno {ficha[opc][0]} foram {ficha[opc][1]}')
