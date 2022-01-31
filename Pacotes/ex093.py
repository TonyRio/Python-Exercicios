jogador ={}
partidas=[]
jogador['nome']=str(input('digite o nome do jogador :'))
tot = int(input(f'quantas partidas \033[32m{jogador["nome"]}\033[m jogou ? '))
for c in range (0,tot):
    partidas.append(int(input(f'quantos gols {jogador["nome"]} fez na {c+1}a. partida ? ')))
jogador['gols']=partidas[:]
jogador['total']=sum(jogador["gols"])
print('\033[31m-=\033[m'*30)
print(f'O nome do Jogador é :\033[32m {jogador["nome"]}\033[m')
print(f'O {jogador["nome"]} jogou {tot} partidas')
for p, g in enumerate (jogador["gols"]):
    print(f'Na Partida => {p+1}  fez {g} gols')
print(f'Com um total de {sum(jogador["gols"])} gols')

print(' Bela Partida !!')

