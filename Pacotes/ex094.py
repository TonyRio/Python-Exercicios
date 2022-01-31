pessoa={}
galera=[]
soma=media=mulheres=0
while True:
    pessoa['nome']=str(input('digite o nome da pessoa : '))
    while True:
        pessoa['sexo']=str(input('digite o sexo (M)/(F) : ')).strip().upper()[0]
        if pessoa['sexo'] in 'mMfF':
            break
        print('\033[31m"erro"\033[m digite somente M ou F :')
    if pessoa['sexo']=='F':
        mulheres= mulheres+1
    pessoa['idade']=int(input('Digite a idade :'))
    soma=(pessoa['idade'])+soma
    galera.append(pessoa.copy())
    while True:
        loop=str(input('quer cotinuar ? S/N - :')).strip().upper()[0]
        if loop in 'nNsS':
            break
        print('** erro ** DIGITE SOMENTE S ou N : ')
    if loop == 'N':
            break
print('\033[32m*-*-\033[m'*10)
print (f'temos cadastrados {len(galera[0])} pessoas')
print(f'a soma das Idades são {soma}')
print(f'a média de idade  são  {soma/len(galera[0]):.0f} anos')
print(f'as mulheres cadastradas foram {mulheres} pessoas ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}',end=' - ')
print()
print('as pessoas acima de 30 anos são :')
for p in galera:
    if p['idade']>=30:
        print(f'{p["nome"]}',end=' - ')
print()
print('\033[32m*-*-\033[m'*10)