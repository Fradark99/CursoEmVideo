def antesu(numero):
    if numero.isdigit():
     numero = int(numero)
     antecessor = numero - 1
     sucessor = numero + 1
     print(f'Seu antecessesor é o {antecessor}, e o seu sucessor é o {sucessor}')
    else:
     print('Digite apenas numeros')
    return numero

numero = input('Digite um numero ')
antesu(numero)
