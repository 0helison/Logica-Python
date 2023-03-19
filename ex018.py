d=(' DESAFIO 18 ')
print('{:=^31}'.format(d))
import math
n=(float(input('Digite o ângulo desejado: ')))
sen=math.sin(math.radians(n))
cos=math.cos(math.radians(n))
tan=math.tan(math.radians(n))
print('Para o ângulo {}º:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(int(n), sen, cos, tan))