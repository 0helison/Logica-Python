#na frase o C equivale a posição 0
frase=' Curso em Video Python '
#1 letra na posição 3
print(frase[3])
#2 letra na posição 3 ate a 12
print(frase[3:13])
#3 letra do inicio ate 12
print(frase[:13])
#4 letra da 13 ate o ultimo
print(frase[13:])
#5 letra na posição 1 ate a 14 pulando 2
print(frase[1:15:2])
#6 letra na posição 1 ate o fim pulando 2
print(frase[1::2])
#7 do inicio ao fim pulando 2
print(frase[::2])
print('='*31)
#quantos 'o' minusculo tem (não conta o "O" maiusculo)
print(frase.count('o'))
#joga toda frase pra maiusculo e depois conta "O"
print(frase.upper().count('O'))
#tsmsnho da frase (conta espaços)
print(len(frase))
#tamanho da frase removendo espaços nas laterais
print(len(frase.strip()))
# a frase é imutavel, mas se quiser alterar de fato a frase
# frase='Curso em Video Python'
# frase= frase.replace('Python', 'Android') - muda permanente
print(frase.replace('Python','Android'))
dividido=frase.split()
#divide a frase e cada palavra vai ser um bloco do 0
print(dividido)
print(dividido[0])
#pega a palavra 2 e mostra a palavra 3 - VídEo
print(dividido[2] [3])
#se tem a palavra curso na farse (true or false)
print('Curso' in frase)

