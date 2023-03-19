op = maior = 0
m = 1
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
while op != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Qual opção você deseja? '))
    if op == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif op == 2:
        m = n1 * n2
        print(f'{n1} X {n2} = {m}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif op == 4:
        print('Informe os novos valores:')
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
    else:
        print('Comando Inválido!')

