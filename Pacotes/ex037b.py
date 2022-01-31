num = int(input('digite um numero para conversão :'))
print('digite a opção escolhida :')
print('''(1) para binária
(2) para Octal
(3) para Hexadecimal''')
opção = int(input(' opção: '))
if opção==1:
    print('o número {} equivale a {} em Binário '.format(num,bin(num)[2:]))
elif opção==2:
    print('o numero {} equivale em Octal {} '.format(num,oct(num)[2:]))
elif opção==3:
    print('o numero {} equivale em hexadecimal {}'.format(num, hex(num)[:2]))
else:
    print('---- inválido ------')
