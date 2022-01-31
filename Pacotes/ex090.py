aluno={}
aluno['nome']= str(input('\033[33mnome do aluno: '))
aluno['media']= float(input(f'Qual a média do  aluno \033[37m{aluno["nome"]} \033[m: '))
if (aluno['media']) >=7:
    aluno['situacao']= 'APROVADO'
elif aluno['media']<7 and aluno['media']>=5:
    aluno['situacao']= 'RECUPERAÇÃO'
else:
    aluno['situacao']='REPROVADO'
print(f'a situação do aluno {aluno["nome"]} é {aluno["situacao"]}')

for k, v in aluno.items():
    print (f' {k} é  = {v}')