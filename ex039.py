d=(' DESAFIO 39 ')
print('{:=^31}'.format(d))
print('='*31)
sex=(str(input('Qual seu sexo? [Masculino ou Feminino]: '))).upper().strip()
if sex == 'FEMININO':
    print('Mulheres não precisam se alistar')
else:
    from datetime import date
    at=date.today().year
    nasc=(int(input('Informe seu ano de nascimento: ')))
    anos= at-nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, anos, at))
    al= nasc + 18
    if anos>18:
        dif = anos - 18
        print('Você deveria ter se alistado há {} anos'.format(dif))
        print('Seu alistamento foi em {}'.format(al))
    elif anos < 18:
        dif = 18- anos
        print('Ainda faltam {} anos para seu alistamento'.format(dif))
        print('Seu alistamento será em {}'.format(al))
    else:
        print('Você deve se alistar IMEDIATAMENTE!')

