mai=men=0
lista=[]
for c in range (0,5):
    lista.append(int(input(f'digite um numero na posição {c} :')))
    if c==0:
        mai=men=lista[c]
    else:
        if lista[c] > mai:
            mai=lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'\033[34mo maior numero é {mai} nas posiçoes :',end='')
for i, v in enumerate   (lista):
    if v==mai:
        print(f'{i}...',end='')
print(f'\n\033[33mmenor valor é {men} nas posições :',end='')
for i,v in enumerate    (lista):
    if v == men:
        print(f'{i}...',end='')
print(f'\033[31m\nvocê digitou os numeros {lista}:')
