from datetime import datetime
dados={}
dados['nome']=str(input('digite o nome :'))
nasc=int(input('Ano de Nascimento :'))
dados['idade']=datetime.now().year - nasc
dados['ctps']= int(input(' numero da CTPS se não tiver digite 0:'))
if dados['ctps']!= 0:
    dados['contratacao']=int(input('ano de contratação :'))
    dados['salário']=float(input('qual o salário ? : R$ '))
    dados['aposentadoria']= dados['idade']+ (dados['contratacao']+35) - datetime.now().year
print('\033[31m-='*30)
for k, v in dados.items():
    print (f'- {k} é  {v}')