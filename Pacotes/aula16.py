lanche='Sabonete','toalha', 'pasta de dente', 'chinelo'
for c in range (0, len(lanche)):
    print (c, lanche[c],'---')
print('\033[31m**\033[m'*18)
for pos, comida in enumerate (lanche):
     print(f'na posicão {pos}',comida)