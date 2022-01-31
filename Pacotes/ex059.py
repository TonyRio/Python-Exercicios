num1 = int(input('Digite 1o. numero :'))
num2 =int(input('Digite o 2o. numero :'))
opcao=0
while opcao!=5:
    opcao = int(input('''
\033[34mO QUE QUER FAZER COM ESSES NÚMERO ?\033[m
    \033[35m=-=-=-=-=-=-=-=-=-=-=-=
    = (1) somar           =
    = (2) multiplicar     =
    = (3) maior numero    =
    = (4) novos numeros   =
    = (5) SAIR            =
    =-=-=-=-=-=-=-=-=-=-=-=\033[m -> '''))
    if opcao == 1:
        print('A Soma entre {} e {} deu {}'.format(num1, num2, num1+num2))
    if opcao ==2:
       print( 'a Multiplicação entre {} e {} deu {}'.format(num1, num2, num1 *num2)  )
    if opcao==3:
        if num1 > num2:
            print('o primeiro número {} é maior que o segundo numero {}'.format(num1, num2))
        if num1==num2:
            print(' o numero  {} e o numero  {} são iguais '.format(num1, num2 ))
        else:
                print(' o primeiro número {} é menor que o segundo número {}'.format(num1, num2))
    elif opcao==4:
        num1= int(input('Digite um novo 1o. numero : '))
        num2= int(input('digite um novo 2o. numero : '))
print(" \033[31m ** FIM DO PROGRAMA, VOLTE SEMPRE !! **")

