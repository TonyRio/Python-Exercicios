v = float(input('qual a distancia de sua viagem em KM ? : '))
v1 = v*0.45
v2 = v*0.50
if v<=200:
    print('sua viagem vai custar R${:.2f}'.format(v2))
else:
    print('sua viagem é mais longa mas custará R$ {}'.format(v1))
print('\nBoa Viagem !')
