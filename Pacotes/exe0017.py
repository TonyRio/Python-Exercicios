'''co = float (input('digite a medida do cateto oposto do triangulo :'))
ca = float (input('digite agora a medida do cateto adjacente do triangulo :'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(' essa é a hipotenusa do triangulo {:.2f} '.format(hi))
'''
from math import hypot
co = float(input('cateto oposto :'))
ca = float (input('cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa do triangulo é : {:.2f}'.format (hi))
