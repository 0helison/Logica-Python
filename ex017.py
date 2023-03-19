d=('DESAFIO 17')
print('{:=^31}'.format(d))

n1=float(input('Informe o comprimento do cateto oposto: '))
n2=float(input('Informe o comprimento do cateto adjacente: '))
f=((n1**2) + (n2**2)) ** (1/2)
print('A hipotenusa vale {:.2f} '.format(f))

import math
n1=float(input('Informe o comprimento do cateto oposto: '))
n2=float(input('Informe o comprimento do cateto adjacente: '))
f=math.hypot(n1, n2)
print('A hipotenusa vale {:.2f} '.format(f))

from math import hypot
n1=float(input('Informe o comprimento do cateto oposto: '))
n2=float(input('Informe o comprimento do cateto adjacente: '))
f=hypot(n1, n2)
print('A hipotenusa vale {:.2f} '.format(f))