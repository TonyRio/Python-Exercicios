from time import sleep
v= int(input('bom dia, digite a sua velocidade: '))
sleep (1)
if v<=80:
    print('-=-' * 15)
    print(' dirija com cuidado, e tenha uma boa viagem !')
    print('-=-'*15)
else:
    print('você está acima da velocidade, e será multado em R$ 7,00 por Km Acima:')
    print('a velocidade permitida é 80KM e pagará {} x R$ 7,00 com total de R${},00 de multa'.format(v-80,(v-80)*7))

print('\ntenha um bom dia e atenção para não ter acidentes !!')
