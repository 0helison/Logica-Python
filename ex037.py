d=(' DESAFIO 37 ')
print('{:=^31}'.format(d))
print('='*31)
n=(int(input('Digite um número inteiro: ')))
print('Escolha um das bases para conversão: ')
print('[1] converter BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
r=(int(input('Sua opção: ')))
if r==1:
    print('{} em BINÁRIO vale {}'.format(n, bin(n)[2:]))
elif r==2:
    print('{} em OCTAL vale {}'.format(n, oct(n)[2:]))
elif r==3:
    print('{} em HEXADECIMAL vale {}'.format(n, hex(n)[2:]))
else:
    print('COMANDO INVÁLIDO!')