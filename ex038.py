d=(' DESAFIO 38 ')
print('{:=^31}'.format(d))
print('='*31)
n1=(int(input('Digite o 1º valor: ')))
n2=(int(input('Digite o 2º valor: ')))
if n1>n2:
    print('O PRIMEIRO valor é maior')
elif n2>n1:
    print('O SEGUNDO valor é maior')
#elif n1==n2:
else:
    print('Os dois valores são IGUAIS.')