print('{:*^60}'.format(' LOJAS TONY '))
preço = float(input('preço das compras : R$ '))
print('''FORMAS DE PAGAMENTO
( 1 ) À VISTA (CHEQUE OU DINHEIRO)
( 2 ) À VISTA NO CARTÃO
( 3 ) 2 X NO CARTÃO
( 4 ) 3 X OU MAIS NO CARTÃO''')
print('{}'.format('_'*30))
opção = int(input('Qual a opção ? :'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço /2
    parcela = total/2
    print('O valor de suas compras R$ {}ficará em 2 parcelas de R$ {:.2f} sem juros'.format(preço, parcela))
elif opção == 4 :
    total = preço + (preço*20/100)
    qpar = int(input('quantidade de parcelas :'))
    print('o valor de de suas compras {} ficará em {} parcelas de R$ {} com juros ' .format(preço, qpar, total/qpar))
else:
    total = preço
    print('********* opção inválida ********* !')
print('O valor da sua compra R$ {:.2f} ficará em R$ {:.2f} '.format(preço, total,))