d=(' DESAFIO 30 ')
print('{:=^42}'.format(d))
print('               PAR OU ÍMPAR ')
print('='*42)
n1=(int(input('Digite um número: ')))
if n1 % 2 == 0:
    print('{} é Par'.format(n1))
else:
    print('{} é Ímpar'. format(n1))