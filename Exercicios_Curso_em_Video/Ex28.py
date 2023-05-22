import random
numero_usuario = int(input('Digite um numero de 0 a 10'))

numero_aleatorio = random.randint(0, 10)

if numero_usuario == numero_aleatorio:
    print('Parabens, você acertou o numero')
else:
    print(' GAME OVER, você errou o numero')

print('O numero que eu pensei foi {}'.format(numero_aleatorio))
