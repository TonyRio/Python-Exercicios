galera=[]
while True:
    galera.append(str(input('digite o seu nome :')))
    galera.append(int(input('digite sua idade :')))
    galera.append(str(input('Qual o estado que nasceu ? :')))
    loop=str(input('Quer continuar ? S/N :'))
    if loop in 'nN':
            break
print(f'_-_'*10)
for c in galera:
    print(f'os candidatos sao : {galera[0]} com {galera[1]} de idade e nascido em {galera[2]}')
c=c+1



