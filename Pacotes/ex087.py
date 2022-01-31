matriz =[[0,0,0],[0,0,0],[0,0,0]]
par=impar=mai=valor=scol=0
for l in range (0,3):
    for c in range  (0,3):
        matriz[l][c] = int(input(f'digite o numero de matriz [{l} - {c}]'))
        if matriz[l][c]%2==0:
            par=par+matriz[l][c]
        else:
            impar=impar+matriz[l][c]
print('\033[34m-=\033[32m'*20)
for p in range (0,3):
    for q in range (0,3):
        print(f'[{matriz[p][q]:^5}]',end='')
    print()
print(f'\033[34ma soma dos numeros pares dá : {par}  \033[32me  impares {impar}')
print('\033[34m-=\033[32m'*20)
for l in range (0,3):
    scol+=matriz[l][2]
print(f'a soma da coluna 3 é : {scol}')
for c in range (0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c] >mai:
            mai=matriz[1][c]
print(f'o maior numero da linha 2 é {mai}')
print('\033[34m-=\033[32m'*20)
