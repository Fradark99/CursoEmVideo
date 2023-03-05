def calculando(a):
    if a.isdigit:
        a = int(a)
        dobro = a * 2
        triplo = a * 3
        raiz = a ** 0.5
        print(
            f'O dobro de {a} é {dobro}', '\n'
            f'O triplo de {a} é {triplo}', '\n'
            f'A raiz de {a} é {raiz}'

        )
    else:
        print('Digite apenas numero')
    return a

numero = input('Digite um numero')
calculando(numero)