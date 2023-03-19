d=(' DESAFIO 40 ')
print('{:=^31}'.format(d))
print('='*31)
n1=(float(input('Informe a 1º nota: ')))
n2=(float(input('Informe a 2º nota: ')))
m=(n1+n2)/2
print('Com as notas {:.1f} e {:.1f} a média do aluno é igual a {:.1f}'.format(n1, n2, m))
if m<5:
    print('Aluno está REPROVADO')
elif m>=5 and m<7 :
    print('Aluno em RECUPERAÇÃO')
elif m>7:
#else:
    print('Aluno APROVADO')

