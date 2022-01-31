lista = list()
for c in range (0,5):
    n=int(input('digite um valor :'))
    if c==0 or n>lista[-1]:
        lista.append(n)
        print('\033[31madicionado ao final da lista\033[m')
    else:
        pos=0
        while pos <len(lista):
            if n <=lista[pos]:
                lista.insert(pos, n)
                print(f'o valor foi colocado na posição {pos}')
                break
            pos=pos+1

print(lista)