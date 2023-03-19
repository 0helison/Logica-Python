n1 = int(input('1º termo da PA: '))
r = int(input('Qual a razão da sua PA? '))
termos = 10
c = 1
total = 0
while termos != 0:
    total += termos
    while c <= termos:
        print(f'{n1} →', end=' ')
        n1 += r
        termos -= 1
    print('PAUSA')
    termos = int(input('Quantos números você que a mais ?'))
print(f'Foram mostrados {total} valores.')
print('FIM DO PROGRAMA!!!')