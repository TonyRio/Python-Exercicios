from random import randint
from time import sleep
print('-='*30)
print(f'   \033[31m             JOGA NA MEGA SENA  \033[m ')
print('-='*30)
jogos=[]
lista=[]
quant = int(input('Quantos jogos quer fazer ? :'))
tot=1
while tot<=quant:
    cont = 0
    while True:
        lista.sort()
        num = randint(1,60)
        if num not in (lista):
            lista.append(num)
            cont=cont+1
        if cont>=6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot=tot+1
print(f' SORTEANDO  {tot-1} JOGOS ......')
sleep(1)
for i, l in enumerate (jogos):

    print(f'\033[34mo jogo {i+1}o. é : \033[35m{l}')
    sleep(0.5)

