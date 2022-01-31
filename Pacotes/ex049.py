n = int(input('qual a tabuada que quer imprimir ?'))
print('**'*10)
for c in range(1,11, 1):
    print(' {:^}  *  {:^} = {:^}       *'.format (c,n, c*n))
print('**'*10)