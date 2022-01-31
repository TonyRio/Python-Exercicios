pc = float(input('Digite o preço do Produto R$ '))
desc = float(input('digite o desconto %  '))
novo = pc - (pc * (desc / 100))
print('O Valor total ficará : R$ {:.2f}'.format(novo))
