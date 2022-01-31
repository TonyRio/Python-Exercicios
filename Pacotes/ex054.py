cont =0
cont2=0
from datetime import date
atual = date.today().year
for c in range  (1,8):
    nasc = int(input('Digite a data de nascimento {} : '.format(c)))
    idade = atual- nasc
    if idade>=21:
        cont+=1
    else:
        cont2+=1
print(' temos {} maiores de Idade e {} menores de idade'.format(cont, cont2))
