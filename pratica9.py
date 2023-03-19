n1 = s = t =0
while True:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    s += n1
    t += 1
#print('O total de valores digitados foi {} e a soma entre eles é igual a {}'.format(t, s))
print(f'O total de valores digitados foi {t} e a soma entre eles é igual a {s}')