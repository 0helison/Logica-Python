d=(' DESAFIO 42 ')
print('{:=^31}'.format(d))
print('='*31)
l1=(float(input('Informe o 1º segmento: ')))
l2=(float(input('Informe o 2º segmento: ')))
l3=(float(input('Informe o 3º segmento: ')))
print('='*31)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM formar um triângulo', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        #(igual é inclusivo, diferença não, por isso tem que comparar l3 != l1
        print('ESCALENO')
    elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
    #else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo ')