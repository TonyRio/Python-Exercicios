num = int(input('informe um nomero de até 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 100 % 10
print('analizando o numero {} '.format(num))
print('a unidade é  :{}'.format(u))
print(' a dezena é  :{}'.format(d))
print(' a centena é :{}'.format(c))
print(' a milhar é  :{}'.format(m))
##print('a milhar é  {}'.format(nstr[0]))
##print('a centena é {}'.format(nstr[1]))
##print('a dezena é  {}'.format(nstr[2]))
##print('a unidade é {}'.format(nstr[3]))
