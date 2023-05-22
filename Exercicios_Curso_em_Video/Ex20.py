#Seleciona uma ordem aleatória para apresentação de trabalhos
import random
n1 = input("Digite o nome do aluno: ")
n2 = input("Digite o nome do aluno: ")
n3 = input("Digite o nome do aluno: ")
n4 = input("Digite o nome do aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será: ", lista)