print('='*19)
print(' LOJA HIPERMANÍACA')
print('='*19)
soma = c = tot = menor = 0
produtom= ''
while True:
    p = str(input('Produto: ')).upper().strip()
    v = float(input('Preço: R$ '))
    resp = ' '
    soma += v
    c += 1
    if c == 1 or v < menor:
        menor = v
        produtom = p
    if v > 1000:
        tot += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'A soma de suas compras deu R$ {soma:.2f}')
print(f'Temos {tot} produtos com valores acima de R$ 1000.00')
print(f'O produto mais barato foi {produtom} e custou R$ {menor:.2f}')
