d=(' DESAFIO 29 ')
print('{:=^42}'.format(d))

print('             RADAR ELETRÔNICO ')
print('='*42)

v=(int(input('Qual a velocidade atual do carro? Km/h ')))
print('='*42)
if v > 80:
    print('-MULTADO! Você excedeu o limite de velocidade de 80 Km/h.')
    m=(v-80)*7
    print('-Você deverá pagar uma multa de R$ {}!'.format(m))
print('-Tenha um bom dia! Dirija com segurança!')
print('='*42)