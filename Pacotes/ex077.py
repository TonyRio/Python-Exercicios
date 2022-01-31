from pyfiglet import figlet_format
print(figlet_format('I c e c o o l  2'))
palavras = ('aprenda','palavras','python','pessoal','computador','abencoada','estudar','programa')
for pos in palavras:
    print(f'\n\033[34mna palavra \033[31m{pos.upper()}\033[m temos vogais :\033[34m ',end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print( letra, end=' ')

