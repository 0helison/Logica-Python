a=int(input('Digite o valor de A: '))
b=int(input('Digite o valor de B: '))
c=int(input('Digite o valor de C: '))
if a < b and a < c and b < c:
    primeiro = a
    segundo = b
    terceiro = c
elif a < b and a < c and c < b:
    primeiro = a
    segundo = c
    terceiro = b
elif b < a and b < c and  a < c:
    primeiro = b
    segundo = a
    terceiro = c
elif b < a and b < c and  c < a:
    primeiro = b
    segundo = c
    terceiro = a
elif c < a and c < b and  a < b:
    primeiro = c
    segundo = a
    terceiro = b
else:
    primeiro = c
    segundo = b
    terceiro = a
print(f'{primeiro} → {segundo} → {terceiro}')
