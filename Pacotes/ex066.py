cont=num=soma=0
while num != 999:
    num=int(input(' \033[34mdigite um numero qualquer : 999 para sair : '))
    if num==999:
        break
    cont=cont+1
    soma=soma+num
print(f'\033[32mforam digitados {cont} numeros')
print(f'\033[37ma soma dos numeros é {soma}')