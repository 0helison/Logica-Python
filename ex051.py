print('='*30)
pa ='10 TERMOS DE UMA PA'
print(f'{pa:^30}')
print('='*30)
n1 = int(input('1º termo: '))
r = int(input('Razão: '))
termo = n1 + (10 - 1) * r
for c in range (n1, termo + r, r):
    print(f'{c} →', end=' ')
print('FIM')

