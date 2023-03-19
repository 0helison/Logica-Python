tot18 = toth = totm = 0
while True:
    print('='*19)
    print('CADASTRE UMA PESSOA')
    print('=' * 19)
    id = int(input('Idade: '))
    sexo = resp = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('=' * 19)
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if id >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and id < 20:
        totm += 1
    if resp == 'N':
        break
print(f'Pessoas com 18 anos ou mais = {tot18}\nTotal de homens = {toth}\nTotal de mulheres com menos de 20 anos = {totm}')
