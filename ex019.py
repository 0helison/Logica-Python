d=(' DESAFIO 19 ')
print('{:=^31}'.format(d))
print('='*31)
from random import choice
n1=(input('Digite o 1º nome: '))
n2=(input('Digite o 2º nome: '))
n3=(input('Digite o 3º nome: '))
n4=(input('Digite o 4º nome: '))
n5=(input('Digite o 5º nome: '))
n=[n1, n2, n3, n4]
e=choice(n)
print('O (a) escolhido(a) foi {}'.format(e))