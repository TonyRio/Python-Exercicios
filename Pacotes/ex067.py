while True:
    num = int(input(' \033[32mDigite a Tabuada que quer visualisar : '))

    print('\033[34m---'*15)
    if num<0:
        break
    for cont in range(1,11):
        print(f'{num} x {cont} = {num*cont}')
    print('\033[34m---'*15)
print('\033[31m*** programa tabuada encerrado !! ***')
print('\033[31m---'*15)
