d=(' DESAFIO 28 ')
print('{:=^42}'.format(d))
print('-=-'*14)
print(' Adivinhe em que número estou pensando ')
print('-=-'*14)
from random import randint
from time import sleep
n=randint(0,5)
r=(int(input('Informe seu número escolhido entre 0 e 5: ')))
print('PROCESSANDO...')
sleep(1)
if n==r:
    print('GANHOUUU! Você digitou {} e eu também pensei em {}.'.format(r, n))
else:
    print('PERDEU, HAHAHAHA! Você digitou {} e eu pensei em {}.'.format(r, n))