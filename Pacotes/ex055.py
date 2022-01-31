maior= 0
menor =0
for c in range  (1,8):
    peso=float(input('digite o peso da {}a. pessoa :'.format(c)))
    if c==1 :
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('o Maior peso é {} e o Menor peso é {}'.format(maior, menor))
