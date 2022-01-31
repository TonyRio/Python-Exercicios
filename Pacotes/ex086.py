matriz =[[0,0,0],[0,0,0],[0,0,0]]
valor=0
for l in range (0,3):
    for c in range  (0,3):
        matriz[l][c] = int(input(f'digite o numero de matriz [{l} - {c}]'))
print('\033[34m-=\033[32m'*20)
for p in range (0,3):
    for q in range (0,3):
        print(f'[{matriz[p][q]:^5}]',end='')
    print()