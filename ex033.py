d=(' DESAFIO 33 ')
print('{:=^31}'.format(d))
print('='*31)
n1=(int(input('Digite um valor: ')))
n2=(int(input('Digite outro valor: ')))
n3=(int(input('Digite outro valor: ')))
#if n1 > n2 and n1 > n3: pode ficar ou não, vc escolhe
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('Maior: {}\nMenor: {}'.format(maior, menor))