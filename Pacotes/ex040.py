n1 = float(input('digita a primeira nota : '))
n2 =float(input('digite a segunda nota : '))
media = (n1+n2)/2
if media >=6 and media <=10:
    print('o aluno obteve média {:.1f} e foi aprovado'.format(media))
elif media<6 and media>=5:
    print('sua média foi baixa {} e você está de recuperação'.format(media))
else:
    print( ' a media ficou em {} Você está reprovado !!'.format(media))
