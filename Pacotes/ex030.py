n = int(input('digite um numero : '))
n1 = n%2
if n1==0:
    print('|-_-_-_|'*4)
    print('| Esse número {} é Par |'.format(n))
    print('|-_-_-_|' * 4)
else:
    print('esse numero {} é Impar'.format(n))