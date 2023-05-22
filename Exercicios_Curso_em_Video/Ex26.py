frase = input('Digite uma frase').upper().strip()
letterA = 0
#print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

for i in frase:
    if i == 'A':
        letterA += 1
    else:
        pass
print('A letra A aparece', letterA, 'vezes na frase')
print('A primeira letra A apareceu na posição', frase.find('A')+1)
print('A ultima letra A apareceu na posição', frase.rfind('A')+1)