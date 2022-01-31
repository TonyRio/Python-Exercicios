temp = []
princ=[]
maior=menor=0
while True:
    temp.append(str(input('digite o nome :')))
    temp.append(int(input('Digite o Peso :')))
    if len(princ)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]

    princ.append(temp[:])
    temp.clear()

    loop = str(input('quer continuar ? S/N : '))
    if loop in 'nN':
        break
print ('-='*12)
print(f'\033[mao todo você cadastrou  {len(princ)} pessoas')
print(f'os mais pesados com  {maior} Kg são :',end='')
for p in princ:
    if p[1]  == maior:

        print(f' {p[0]} ',end='')
print(f'\nos mais Leves com  {menor} Kg são :',end='')
for p in princ:
    if p[1]  == menor:

        print(f' {p[0]} ',end='')

