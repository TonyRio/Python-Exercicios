from pyfiglet import figlet_format
extenso = 'zero','um', 'dois', 'tres', 'quatro', 'cintco', 'seis', 'sete', 'oito', 'nove', 'dez'
print(figlet_format('I c e c o o l  2'))
lista = ('lapis', 2.30, 'caneta',2 ,'regua', 4.6,'mochila', 34.90,'canetinha',12.80)
print('--'*19)
print(f'{"LISTA DE PREÇOS":^40}')
print('--'*19)

for pos in range  (0,len(lista))  :
    if pos%2==0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('--' * 19)
