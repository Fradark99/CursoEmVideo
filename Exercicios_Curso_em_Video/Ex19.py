#Escolhe aleatoriamente um aluno.
import random
aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aleatorio = random.choice([aluno1, aluno2, aluno3])
print("O aluno escolhido foi {}".format(aleatorio))
