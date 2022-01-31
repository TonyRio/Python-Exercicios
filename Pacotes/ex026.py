frase = str(input('digite uma frase :')).strip().upper()
print ('a frase possui {} letras (A)'.format(frase.count('A')))
print(' a primeira letra (A) aparece na posição {}'.format(frase.find('A')+1))
print('a ultima letra (A) aparece na posição {}'.format(frase.rfind('A')+1))