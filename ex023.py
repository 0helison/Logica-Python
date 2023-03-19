d=(' Desafio 23 ')
print('{:=^31}'.format(d))
print('='*31)
n1=(int(input('Digite um número de 0 a 9999: ')))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Analisando {} ->>>\nUnidade: {:3}\nDezena: {:4}\nCentena: {:3}\nMilhar: {:4}'.format(n1, u, d, c, m))