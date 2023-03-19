t = soma = 0
while True:
    c = int(input('Digite um valor (999 para parar): '))
    if c == 999:
        break
    t += 1
    soma += c
print(f'A soma dos {t} é igual a {soma}')