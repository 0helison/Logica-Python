resp='S'
soma = tot = maior = menor = c = 0
while resp == 'S':
    n1 = int(input('Digite um número: '))
    c += 1
    tot += 1
    soma += n1
    if c == 1:
        maior = menor = n1
    else:
        if n1 > maior:
                maior = n1
        if n1 < menor:
                menor =n1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = soma/tot
print(f'Valores digitados: {tot}\nMédia: {m:.2f}\nMaior valor: {maior}\nMenor valor: {menor}')