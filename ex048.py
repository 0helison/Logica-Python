s=0
n=0
for c in range (1,501,2):
    if c % 3 ==0:
        s = s + c
        n = n +1
print('A soma dos {} valores é igual a {}'.format(n, s))