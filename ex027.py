d=(' Desafio 27 ')
print('{:=^31}'.format(d))
print('='*31)
n=str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer, {}!'.format(n))
ne=n.split()
print('Seu primeiro nome é {}'.format(ne[0]))
g=n.split()
print('Seu último nome é {}'.format(g[len(g)-1]))


