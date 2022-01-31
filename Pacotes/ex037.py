casa = float    (input('digite o valor da casa : R$ '))
salario = float(input('digite o sálario atual : R$ '))
prazo = int(input('diagite qual o prazo de compra : anos - '))
parcelas = (prazo*12)
minimo = salario *(30/100)
vparcela= (casa/parcelas)
if vparcela <=  minimo:
        print('para pagar uma casa no valor de R$ {:.2f}  serão  {:.0f} parcelas de  R$ {:.2f}'.format(casa, parcelas, vparcela))

else:
        print(' não será possivel o financiamento !!')

print('minimo salario para financiamento : R$ {:.2f}'.format(minimo))