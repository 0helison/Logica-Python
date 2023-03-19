d=(' DESAFIO 31 ')
print('{:=^42}'.format(d))
print('               PAR OU ÍMPAR ')
print('='*42)
n1=float(input('Qual a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {} Km'.format(n1))
if n1 >= 200:
    p=n1*0.45
else:
    p=n1*0.5
print('O preço da sua viagem será R$ {:.2f}'.format(p))