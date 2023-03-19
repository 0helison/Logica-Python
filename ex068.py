print('-'*51)
d = 'JOGO - PAR OU ÍMPAR?'
print(f'{d:^51}')
print('-'*51)
tot = 0
while True:
    from random import randint
    pc = randint(0, 11)
    resp = ' '
    while resp not in 'PI':
        resp = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    n1 = int(input('Escolha um valor: '))
    print('-'*51)
    soma = n1 + pc
    print(f'Você jogou {n1} e o computador {pc}. Soma = {soma}', end=' ')
    print('= PAR' if soma % 2 == 0 else '= ÍMPAR')
    print('-' * 51)
    if soma % 2 == 0 and resp == 'P' or soma % 2 == 1 and resp == 'I':
        tot += 1
        print('Você VENCEU! Vamos jogar novamente...')
    else:
        break
print('Você PERDEU! Game over...')
print(f'Você venceu {tot}x')
print('-'*51)

