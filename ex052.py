n1 = int(input('Digite um número: '))
td = 0
for c in range (1, n1+1):
    if n1 % c == 0:
        print(f'\033[33m{c}',end=' ')
        td += 1
    else:
        print(f'\033[31m{c}', end=' ')
print('')
print(f'\033[38mO número {n1} foi divísivel {td} vezes',end=' ')
if td > 2:
    print('\033[38me por isso ele NÃO É PRIMO')
else:
    print('\033[38me por isso ele É PRIMO')





