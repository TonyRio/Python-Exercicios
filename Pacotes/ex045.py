from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0,2)
#print('o PC escolheu o numero {}'.format(itens[pc]))
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador= int(input(' qual a sua escolha ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !')
print('++'*18)
print(' O computador escolheu ** {:^}  **'.format(itens[pc]))
print(' Você escolheu         -- {:^}  --'.format(itens[jogador]))
print('++'*18)
g = ('O JOGADOR GANHOU')
p = ('O COMPUTADOR GANHOU')
if pc == 0 and jogador==1:
    print(g)
elif pc == 1 and jogador == 2:
    print(g)
elif pc==2 and jogador ==0:
    print(g)
elif pc == jogador:
    print('JOGO EMPATADO')
else:
    print(p)
