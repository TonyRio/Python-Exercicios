peso = float(input('qual o peso da pessoa ?  '))
altura = float(input('qual a altura da pessoa ?  '))
imc = peso/(altura ** 2)
print(' o indice de massa corporal é {:.1f} '.format(imc))
if imc <18.5:
    print(' =-='*8 )
    print(' a pessoa está abaixo do peso.')
    print(' =-=' *8)
elif 18.5 <= imc < 25:
    print(' =-=' * 5)
    print('parabens, voce esta com o peso normal')
elif 25 <= imc <30:
    print(' =-=' * 5)
    print('voce está com sobrepeso')

