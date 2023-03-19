d=('DESAFIO 8')
print('{:=^21}'.format(d))
n=float(input('Digite o valor, em metros, que você quer converter: '))
km=n/1000
hm=n/100
dam=n/10
dm=n*10
cm=n*100
mm=n*1000
print('{} M corresponde a:\n{:.3f} Km\n{:.2f} Hm\n{:.1f} Dam\n{:.1f} Dm\n{:.1f} Cm\n{:.1f} Mm'.format(n, km, hm, dam, dm, cm, mm))