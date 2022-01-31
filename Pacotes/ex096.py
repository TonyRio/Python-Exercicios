def area (larg, comp):
    a=larg*comp
    print(f'a area do terreno {larg} e {comp} = {a}m2. ')

print('CONTROLE DE TERRENOS')
print('-='*30)
l=float(input('digite a Largura : '))
c=float(input('digite agora o comprimento: '))
area(l, c)