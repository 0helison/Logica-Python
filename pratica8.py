c = 1
while c < 11:
    print(c, end=' ')
    c += 1
print ('')

n=1
totpar = totimpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            totpar+=1
        else:
            totimpar+=1
print('Total de Pares: {}\nTotal de Ímpares: {}'.format(totpar, totimpar))
print('='*20)

r= 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar ? [S/N] ' )).upper()
print('Fim')
print('='*20)
