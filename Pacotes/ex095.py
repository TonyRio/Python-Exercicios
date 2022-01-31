jogador ={}
partidas=[]
time=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('digite o nome do jogador :'))
    tot = int(input(f'quantas partidas \033[32m{jogador["nome"]}\033[m jogou ? '))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f'quantos gols {jogador["nome"]} fez na {c+1}a. partida ? ')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        loop=str(input('Quer continuar ? [S/N] :')).strip().upper()[0]
        if loop in 'nNsS':
           break
        print('Digite somente S ou N ')
    if loop == 'N':
        break
print('--'*22)
print('cod  ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('--'*22)
for k, v in enumerate(time):
    print(f'{k:>3}  ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('--'*22)
while True:
    busca=int(input('Qual jogador quer mostrar  ? : (999 para sair) -> '))
    if busca==999:
        break
    if busca >= len(time):
        print('\033[31mNÃO EXISTE ESSE JOGADOR\033[m !')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, k in enumerate(time[busca]['gols'] ):
            print(f'na {i+1}a. partida  fez  {k} gols')


print('\n < VOLTE SEMPRE !! >')