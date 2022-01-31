soma=0
cont=0
for c in range  (1,7):
    n = int(input('digite o {} número aqui : '.format(c)))
    if n%2==0:
        soma = soma+n
        cont = cont+1
print(' a soma de {} numeros pares deu {} '.format(cont, soma))

