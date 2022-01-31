from pyfiglet import figlet_format
extenso = 'zero','um', 'dois', 'tres', 'quatro', 'cintco', 'seis', 'sete', 'oito', 'nove', 'dez'
print(figlet_format('I c e c o o l  2'))
while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if 0<=num<=10:
        break
    print('\033[31mtente novamente ', end='')
print(f'o numero digitado foi {num} em \033[32mextenso {extenso[num]}')

while True:
    loop = str(input('Você quer continuar ?  (S/N) :')).strip().upper()[0]
    if loop == 'S':
        num = int(input('Digite um numero entre 0 e 10: '))
        while True:
            if 0<=num<=10:
                print(f'o numero digitado foi {num} em \033[32mextenso {extenso[num]}')
                break
            print('\033[31mtente novamente ', end='')

            break
    else:
        break
        mk850
        mk 295
        mk 345
        540