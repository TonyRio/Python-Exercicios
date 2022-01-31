def dobra(lst):
    pos=0
    while pos <(len(lst)):
        lst[pos] *=10
        pos=pos+1


valores=[2, 3, 4, 5, 7, 23]
print(valores)
dobra(valores)
print(valores)

