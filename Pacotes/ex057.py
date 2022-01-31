sexo= str(input('digite o sexo da pessoa \033[36m(M/F)\033[m: ')).upper().strip()[0]
while sexo not in 'MmfF':
    sexo=str(input(' \033[32mdados inválidos, digite qual o sexo\033[m (M/F :')).strip().upper()
print(sexo)

