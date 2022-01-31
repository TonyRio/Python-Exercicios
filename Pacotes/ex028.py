from random import randint
from time import sleep

n = randint(0,5)
print('O Computador pensou em um número entre 0 e 5 \n         tente adivinhar.'.format(n))
n1 = int(input('Digite o numero que ele pensou :'))
print('PENSANDO.......')
sleep(2)
if n==n1:
    print('.`0´.'*10)
    print(' parabéns, você acertou, ele pensou o numero {}\n'.format(n))
else:
    print('*()*'*20)
    print(' tente mais uma vez pois ele pensou no numero {} e você errou\n'.format(n))
    print(' valeu o jogo')


