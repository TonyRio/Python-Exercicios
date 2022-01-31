print('\033[33m<>|<>'*10)
print('{:^44}'.format('++ Banco Icecool ++ -2'))
print('\033[33m<>|<>'*10)
valor= int(input('Que valor você quer sacar ? R$ '))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total=total-ced
        totced=totced+1
    else:
        if totced>0:
            print(f'o total de cedulas é {totced} de {ced}')
        if ced==50:
            ced=20
            totced = 0
        elif ced==20:
            ced=10
            totced = 0
        elif ced==10:
            ced=5
            totced = 0
        elif ced==5:
            ced=2
            totced = 0
        elif ced==2:
            ced=1
            totced=0
            if total==0:
                break
print('OBRIGADO POR UTILIZAR NOSSO SISTEMA !')




