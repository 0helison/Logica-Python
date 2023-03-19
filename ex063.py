n = int(input('Quantos termos você quer ver? '))
a1 = 0
c = a2 = 1
print(f'{a1} → {a2} → ', end='')
while c <= (n - 2) :
    a3 = a1 + a2
    print(f'{a3} → ', end='')
    c += 1
    a1 = a2
    a2 = a3
print('Fim')
