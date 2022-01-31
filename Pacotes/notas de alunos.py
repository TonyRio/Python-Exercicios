nt1 = float (input('digite a nota do bimestre 1: '))
nt2 = float (input('digite a nota do bimestre 2: '))
nt3 = float (input('digite a nota do bimestre 3: '))
nt4 = float (input('digite a nota do bimestre 4: '))
md1 = (nt1+nt2+nt3+nt4)/4
print  (' as notas foram : primeiro bimestre :{}\nsegundo bimestre :{}\nterceiro bimestre :{}\nquarto bimestre :{}'.format(nt1,nt2, nt3, nt4))
print ('sua média anual foi : {:.1f}'.format(md1))
print('faltaram  {:.1f} pontos para aprovação.'.format(6.0-md1))