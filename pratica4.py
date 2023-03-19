carro=int(input('Quantos anos o seu carro tem? '))
if carro <= 3:
    print('Seu carro está novo!')
else:
    print('Seu carro está velho!')
print('== Fim ==')

#Outra Forma

carro=int(input('Quantos anos o seu carro tem? '))
print('Seu carro está novo' if carro <= 3 else 'Seu carro está velho')
print('== Fim ==')

nome=str(input('Digite seu nome: ')).upper().strip()
if nome == ('HELISON'):
    print ('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome.title()))

n1=(float(input('Digite sua 1º nota: ')))
n2=(float(input('Digite sua 2º nota: ')))
m=(n1+n2)/2
if m >= 6:
    print('Sua média foi {:.2f}, você se saiu bem. Parabéns'.format(m))
else:
    print('Sua média foi {}, você não se saiu bem. Estude mais!'.format(m))