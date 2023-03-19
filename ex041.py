d=(' DESAFIO 40 ')
print('{:=^31}'.format(d))
print('='*31)
from datetime import date
at=date.today().year
n1=(int(input('Qual o ano de nascimento: ')))
id=(at-n1)
print('O atleta tem {} anos.'.format(id))
if id <= 9:
    print('Classificação: MIRIM')
elif id > 9 and id <=14:
#elif id <= 14: (pelo primeiro se, o python entende que sera acima de 9)
    print('Classificação: INFANTIL')
elif id > 14 and id <= 19:
    print('Classificação: JÚNIOR')
elif id > 19 and id <= 25:
    print('Classificação: SÊNIOR')
#else:
elif id > 25:
    print('Classificação: MASTER')