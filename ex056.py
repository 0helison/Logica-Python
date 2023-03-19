s=0
m=0
maior=0
hmaior=''
t=0
for c in range (1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    id = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    s += id
    if sexo == 'M':
        maior = id
        hmaior = nome
        if id > maior:
            maior = id
            hmaior = nome
    else:
        if id < 20:
            t += 1
m = s/4
print('A média de idade do grupo é de {:.2f} anos.'.format(m))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, hmaior.title()))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(t))

