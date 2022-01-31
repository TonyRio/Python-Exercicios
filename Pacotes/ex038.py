n1= int(input('digite um numero : '))
n2 = int(input('digi um segundo número :'))

if n1<n2:
    print(' o primeiro numero {} é menor que o segundo número {}'.format( n1,n2  ))
elif n1>n2:
    print('o segundo número {} é menor que o primeiro número {}'.format(n2,n1))
elif n1==n2:
    print('os numeros {} e {} são numeros iguais '.format (n1, n2))

