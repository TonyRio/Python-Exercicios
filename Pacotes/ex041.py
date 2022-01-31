from datetime import date

atual = date.today().year
nasc = int(input('digite seu ano de nascimento : '))
idade = atual-nasc
print('você que nasceu em {} tem {} anos de idade.'.format(nasc, idade))
if idade<=9 :
    print('o Atleta com {} anos é da categoria Mirim.'.format(idade))
elif idade>9 and idade <=14:
    print( 'o atleta com {} anos é da categoria Juvenil')
elif idade >14 and idade <=18:
    print ('o atleta com {} anos é da categoria adulto'.format(idade))
else:
    print('o atleta com {} anos é da categoria Senior'.format(idade))
