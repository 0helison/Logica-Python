nome=str(input('Digite seu 1º nome: ')).upper().strip()
if nome == 'HELISON':
    print ('Que nome bonito você tem!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é popular.')
elif nome in 'CLÁUDIA ANA JÉSSICA JULIANA':
    print('Que belo nome feminino.')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome.title()))