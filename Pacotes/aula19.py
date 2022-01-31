estado={}
brasil=[]
for c in range (0,3):
    estado['uf']=str(input('digite o estado :'))
    estado['cidade']=str(input('digite a cidade :'))
    brasil.append(estado.copy())
for e in brasil:
    for a,b in e.items():
        print(f'o campo {a} tem valor {b}',end=' ')
        print()