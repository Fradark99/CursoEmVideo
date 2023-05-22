#Passar um angulo em graus e retornar o seno, cosseno e tangente desse angulo
import math
angulo = float(input("Digite o angulo: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))