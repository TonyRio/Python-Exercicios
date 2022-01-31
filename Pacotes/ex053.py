frase= str(input('digite uma Frase :')).strip() .upper()
palavras = frase.split()
junto =''.join(palavras)
inverso =''
for c in range (len(junto)-1 , -1, -1):
    inverso+= junto[c]
print(junto, '\033[36m', inverso)
if inverso==junto:
    print('\033[33m Ela é um Palindromo !!')
else:
    print('\033[35m Ela não é um palindromo')

