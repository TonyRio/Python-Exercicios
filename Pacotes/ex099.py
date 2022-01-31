from time import sleep
def maior(* num):
    cont =maior=0
    print('\nANALISANDO VALORES.....')
    for valor in num:
        print(f'{valor}',end='-')
        sleep(.5)
        if cont == 0:
            maior=valor
        if valor>maior:
            maior=valor
        cont=cont+1
    print(f'foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 5, 9, 7, 3)
maior(2, 7, 0)
maior(1, 6)
maior(4)
maior()