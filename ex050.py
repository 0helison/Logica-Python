s=0
cont=0
for c in range (1,7):
    n1 = int(input('Digite um valor: ').format(c))
    if n1 % 2 ==0:
        s += n1
        cont += 1
if cont == 1:
    print('Você informou apenas 1 número par de valor {}'.format(s))
elif cont == 0:
    print('Você informou 0 números pares.')
else:
    print('A soma dos {} pares informados é igual a {}'.format(cont, s))