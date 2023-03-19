d=(' DESAFIO 44 ')
print('{:=^31}'.format(d))
print('='*31)
v=(float(input('Informe o valor da sua compra: R$ ')))
print('='*31)
print('''[1] Pagamento à vista em dinheiro ou cheque.
[2] Pagamento à vista no cartão de crédito.
[3] Pagamento em até 2x no cartão de crédito
[4] Pagamento em 3x ou mais no cartão''')
print('='*31)
r=(int(input('Escolha uma opção acima: ')))
if r==1:
    vf=v-(v*10/100)
    print('No final, sua compra de R$ {:.2f} custará R$ {:.2f}'.format(v, vf))
elif r==2:
    vf = v - (v * 5 / 100)
    print('No final, sua compra de R$ {:.2f} custará R$ {:.2f}'.format(v, vf))

elif r==3:
    p=(int(input('Em quantas parcelas você quer dividir? ')))
    if p==1:
        print('Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f} sem juros.'.format(v,p, v))
    elif p==2:
        print('Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f} sem juros'.format(v, p, v/p))
    else:
        print('COMANDO INVÁLIDO <> Tente Novamente!')
elif r==4:
    p=(int(input('Em quantas parcelas você quer dividir? ')))
    if p<3:
        print('COMANDO INVÁLIDO <> Tente Novamente!')
    elif p>=3:
        k = v + (v*20/100)
        print('Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f} com juros'.format(v, p, k/p))
        print('Valor final de R$ {:.2f}'.format(k))
else:
    print('COMANDO INVÁLIDO <> Tente Novamente!')