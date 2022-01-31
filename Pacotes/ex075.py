from pyfiglet import figlet_format
extenso = 'zero','um', 'dois', 'tres', 'quatro', 'cintco', 'seis', 'sete', 'oito', 'nove', 'dez'
print(figlet_format('I c e c o o l  2'))
num = (int(input('digite um numero :')),
        int(input('digite mais um numero :')),
        int(input('digite outro numero :')),
        int(input('digite um numero final :')))
print(f'\033[35mvoce digitou os numeros {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'o numero 3 apareceu na {num.index(3)+1}.a posição')
else:
    print('não foram encontrados nenhum numero 3')
print('\033[32mos valores pasres digitados foram :',end='')
for n in num:
    if n%2==0:
        print(n ,end=',  ')


