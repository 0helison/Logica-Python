frase = str(input('Digite uma frase: ')).upper().strip()
junto = ''.join(frase.split())
inverso = ''
for c in range (len(junto)-1, -1, -1):
   inverso += junto[c]
print(junto, inverso)
if junto != inverso:
   print('Sua frase NÃO É PALÍNDROMO.')
else:
   print('Sua frase É PALÍNDROMO.')
