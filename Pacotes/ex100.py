from random import randint
from time import sleep

def sorteia(lista):
        for cont in  range(0,5):
            n=randint(1,10)
            lista.append(n)
            print(f'{n} ',end='')
            sleep(.5)
        print('pronto')

def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'a soma dos valores pares da lista {lista} resulta  : {soma}',end='')




# def somapar():
numeros=list()
sorteia(numeros)
somapar(numeros)