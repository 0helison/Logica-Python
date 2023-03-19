n1 = int(input('Informe um número para calcular o fatorial: '))
c = t = 1
print(f'Calculando {n1}! = ', end='')
while n1 >= c:
    print(f'{n1}', end='')
    print(' X ' if n1 > 1 else ' = ', end='')
    t = t*n1
    n1 -= 1
print(t)

n2 = int(input('Informe um número para calcular o fatorial: '))
s=1
print(f'Calculando {n2}! = ', end='')
for p in range (n2, 0, -1):
    print(p, end='')
    print(' x ' if p > 1 else ' = ', end='')
    s *= p
print(s)


