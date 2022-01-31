maioridadehomem=0
nomevelho=''
macho=0
femea=0
media=0
for c in range (1,5):
    print('------- {}.a pessoa -------'.format(c))
    nome=str(input('\033[34m Nome: ')).strip()
    idade=int(input('\033[35m Idade: '))
    sexo=str(input('\033[36m Sexo (M/F) :\033[m')).strip()
    media=media+idade
    if sexo in 'Ff' and idade<20:
        femea= (femea+1)
    if c==1 and sexo in 'mM':
        maioridadehomem=idade
        nomevelho=nome
    if sexo  in 'mM' and idade>maioridadehomem:
            maioridadehomem=idade
            nomevelho=nome

print('a media de idade é {}'.format(media/4))
print('o nome do mais velho é {} e tem idade {} anos'.format(nomevelho, maioridadehomem))
print('existem {} mulheres menores de 20 anos'.format(femea))
