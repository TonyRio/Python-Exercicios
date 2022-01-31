from random import randint
from pyfiglet import figlet_format
extenso = 'zero','um', 'dois', 'tres', 'quatro', 'cintco', 'seis', 'sete', 'oito', 'nove', 'dez'
print(figlet_format('I c e c o o l  2'))
num=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'os valores sorteados foram :',end='')
for n in num:
    print(f'{n}',end=' ')
print(f'\n\033[31mo maior valor foi {max(num)}')
print(f'\033[34mo menor valor foi {min(num)}')
