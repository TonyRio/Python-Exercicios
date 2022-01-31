par=0
impar=0
n=1
while n != 0:
    n=int(input('digite um numero :'))
    if n!=0:
        if n%2==0:
            par=par+1
        else:
            impar = impar+1

    print('+++'*4)
print('\033[36m foram digitados {} numeros pares e {} numeros impares\033[m'.format(par, impar))
print('FIM')