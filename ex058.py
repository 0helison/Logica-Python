print('='*63)
print('Acabei de pensar em um número entre 1 e 10, consegue advinhar??')
print('='*63)
from random import randint
s = randint(1, 10)
p = int(input('Qual seu palpite? '))
tot = 1
while p != s:
    tot += 1
    if s > p:
        print('Mais... Tente novamente')
        p = int(input('Qual seu palpite? '))
    elif s < p:
        print('Menos... Tente novamente')
        p = int(input('Qual seu palpite? '))
print('ACERTOU!!!')
print(f'Nº de tentativas: {tot}')
