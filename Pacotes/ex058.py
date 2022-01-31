from random import randint
tentativas=0
pcnum = randint(0,10)
#print('\033[34msou seu PC acabei de pensar no numero {}'.format (pcnum))
print('pensei em um número de 1 a 10, você consegue adivinhar ?\033[m ')
meunum =int(input('digite o numero  : '))
while meunum !=pcnum:
    if meunum!=pcnum:
        tentativas=tentativas+1
        print('\033[31m numero errado\033[m ')
    if meunum>pcnum:

        print('\033[32mtente um numero menor\033[m')
    else:
        print('\033[34mtente numero maior\033[m')

    meunum=int(input('tente novamente digitando aqui :'))
print('\033[35m**'*20)
print('\033[36mPARABÉNS, VOCÊ ACERTOU EM {} TENTATIVAS'.format(tentativas))
print('\033[35m**'*20)