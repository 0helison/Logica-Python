d=(' DESAFIO 34 ')
print('{:=^31}'.format(d))
print('='*31)
s=(float(input('Informe o salário atual do funcionário: R$ ')))
if s <= 1250:
    nv = s + (s*15/100)
else:
    nv = s + (s*10/100)
print('O funcionário que recebia R$ {:.2f} passará a receber R$ {:.2f}'.format(s, nv))
