from random import randint
v=0
pc = randint(0,11)
jogador = int(input('digite um numero : '))
total = pc+jogador
escolha =''
escolha = str(input('Digite a sua escolha se Par ou Impar (P/I) :')).strip().upper()[0]
while escolha not in 'PI':
    escolha = str(input('Digite a sua escolha se Par ou Impar (P/I) :')).strip().upper()[0]
if total%2==1 and escolha=='i':
    print(f' a soma da escolha do PC {pc} + {jogador} deu {total} NÚMERO impar .')
    print('\033[34mVOCÊ GANHOU !!\33[m')
    v=+1
else:
    if total%2==0:
        print(f' a soma da escolha do PC {pc} + {jogador} deu {total} NÚMERO PAR .')
        print('\033[31mO COMPUTADOR GANHOU !!\033[m')

print(f'\033[36mO JOGO TERMINOU E VOCÊ TEVE {v} VITÓRIAS !')


