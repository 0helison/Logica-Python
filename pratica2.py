import math
n=int(input('Digite um número: '))
raiz=math.sqrt(n)
print('A raiz de {} é {:.2f}'.format(n, math.ceil(raiz)))

#2 forma

from math import sqrt, floor
n=int(input('Digite um número: '))
raiz=sqrt(n)
print('A raiz de {} é igual a {:.2f}'.format(n, floor(raiz)))

#3

import random
n=random.random()
print(n)

#4

import random
n=random.randint(1, 10)
print(n)

