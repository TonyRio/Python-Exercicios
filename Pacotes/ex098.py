from time import   sleep
def contador (i, f, p):
    print(f' contagem de {i} até {f} de {p} em {p}')


    if i <f:
        cont = i
        while cont<=f:
            print(f'{cont}',end='-')
            sleep(.5)
            cont+=p
        print('FIM')
    else:
        cont=i
        while cont>=f:
            print(f'{cont}',end='-')
            sleep(.5)
            cont -= p
        print('FIM')


    print('\n-- OBRIGADO --')

ini=int(input('digite o inicio: '))
fin=int(input('digit o final: '))
pas=int(input('digite de quanto em quanto: '))
contador(ini, fin, pas)