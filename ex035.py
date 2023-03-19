d=(' DESAFIO 35 ')
print('{:=^31}'.format(d))
print('='*31)
n1=(float(input('Digite o valor do 1º segmento: ')))
n2=(float(input('Digite o valor do 2º segmento: ')))
n3=(float(input('Digite o valor do 3º segmento: ')))
if n1 + n2 >= n3 and n1 + n3 >= n2 and n2 + n3 >= n1:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')