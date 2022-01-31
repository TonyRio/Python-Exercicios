gastos=caro=barato=cont=0
nomebarato= ' '
while True :
    nome = str(input('Qual o nome do produto ?: ')).upper()
    preço = float(input('Qual o valor do produto ? :R$ '))
    cont=cont+1
    if cont==1:
        barato=preço
        nomebarato=nome
    else:
        if preço<barato:
            barato=preço
            nomebarato=nome

    gastos =preço+gastos
    if preço>=1000:
        caro=caro+1

    loop=' '
    while loop not in 'SN':
        loop = str(input('que continuar ? (S/N)')).strip().upper()[0]
    if loop=='N':
           break
print('\033[36m%%'*40)
print(f'\033[37mA conta tem um total de R$ {gastos:.2f}')
print(f'\033[32mForam achados {caro} produtos com valor maior que R$ 1000.00')
print(f'\033[31mO Produto mais barato é o {nomebarato} que custou R$ {barato:.2f}')

