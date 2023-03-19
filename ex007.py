d=('DESAFIO 7')
print('{:=^21}'.format(d))
nome=input('Informe o nome do aluno: ')
nota1=float(input('Digite a 1º nota: '))
nota2=float(input('Digite a 2º nota: '))
m=(nota1+nota2)/2
print('A média entre as notas {:.1f} e {:.1f} de {} foi igual a {:.1f}'.format(nota1, nota2, nome, m))