d=(' DESAFIO 43 ')
print('{:=^31}'.format(d))
print('='*31)
p=(float(input('Informe seu peso em Kg: ')))
a=(float(input('Informe sua altura em M: ')))
imc = p/(a**2)
print('Seu IMC é igual a {:.1f} e você está '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO IDEAL.')
elif imc < 25:
    print('PESO IDEAL, Parabéns!')
elif imc < 30:
    print('em SOBREPESO.')
elif imc < 40:
    print('em OBESIDADE.')
else:
    print('em OBESIDADE MÓRBIDA.')

