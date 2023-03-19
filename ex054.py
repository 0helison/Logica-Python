from datetime import date
at = date.today().year
dif = totmaior = totmenor = 0
for c in range (1, 8):
    n1 = int(input(f'Em que ano {c}ª pessoa nasceu: '))
    dif = at - n1
    if dif >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Maiores de idade: {totmaior}\nMenores de idade: {totmenor}')