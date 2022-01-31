from random import randint
from time import    sleep
from operator import itemgetter
jogo={'jogador 1': randint(1,6),
      'jogador 2': randint(1,6),
      'jogador 3': randint(1,6),
      'jogador 4': randint(1,6)
      }
ranking=[]
for k, v in jogo.items():
    print(f'o jogador {k} tirou o valor {v}')
    sleep(.8)
ranking= sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print (f'o {i+1}o. {v[0]} tirando numero {v[1]}')
    sleep(.5)

