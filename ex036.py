d=(' DESAFIO 36 ')
print('{:=^31}'.format(d))
print('='*31)
valor=(float(input('Informe o valor da casa a financiar : R$ ')))
ano=(int(input('Em quantos anos você quer financiar? ')))
sal=(float(input('Informe seu salário: R$ ')))
pres=valor/(ano*12)
ex=sal*30/100
print('Para uma casa de R$ {:.2f}, parcelada em {} anos, tem-se prestação mensal de R$ {:.2f}'.format(valor, ano, pres))
if pres > ex:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser APROVADO!')
