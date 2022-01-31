maior=masc=fem=0
while True:
    idade = int(input('Qual a Idade ?'))
    if idade > 18:
        maior = maior + 1
    sexo=' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo ? : (M/F)')).strip().upper()[0]
        if sexo=='M':
            masc=masc+1
    if sexo=='F' and idade<20:
        fem=fem+1
    loop=' '
    loop = str(input(' quer continuar ? (S/N)')).strip().upper()[0]
    if loop == 'N':
        break
    while loop not in 'SN':
        loop = str(input(' quer continuar ? (S/N)')).strip().upper()[0]

print(f'\033[34mhouve {maior} que são maiores de 18 anos')
print(f'houve uma quantidade de {masc} homens')
print(f'\033[31mComo também foram contadas {fem} mulheres menores de 20 anos ')
print('\033[35mACABOU !!')


