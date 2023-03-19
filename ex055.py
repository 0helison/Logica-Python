menor = maior = 0
for c in range (1,6):
    peso = float(input(f'Informe o peso da {c}º pessoa: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Menor peso: Kg {menor}\nMaior peso: Kg {maior}')
