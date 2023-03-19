while True:
    t = int(input('Quer ver a tabuada de que valor: '))
    if t < 0:
        break
    for c in range (1, 11):
        m = t * c
        print(f'{t} X {c:2} = {m}')
        c += 1
print('PROGRAMA ENCERRADO')




