resp = 'S'
media=menor=maior=cont=0
while resp in 'sS':
    n = int(input(' digite um valor :'))
    resp = str(input('Quer continuar ? (S/N)')).upper().strip()[0]
    media=media+n
    cont=cont+1
    if cont ==1:
        maior=menor=n
    if n > maior:
        maior=n
    else:
        if n<menor:
            menor = n
print('\033[35m a media dos {} numeros digitados  é :{:.1f}'.format(cont, media/cont))
print(' o maior numero digitado foi : {} e o menor foi {}'.format(maior, menor))
print('\033[34m**  fim  ** ')
