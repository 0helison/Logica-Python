d=(' DESAFIO 11 ')
print('{:=^31}'.format(d))
print('='*31)
print('       PINTANDO PAREDES')
print('='*31)
l=float(input('Largura da parede em metros: '))
h=float(input('Altura da parede em metros: '))
a=l*h
q=a/2
print('Área: {} x {} = {:.2f}m²'.format(l, h, a))
print('Então, é preciso {:.2f}L de tinta para pintar a área correspondente.'.format(q))
print('='*31)
