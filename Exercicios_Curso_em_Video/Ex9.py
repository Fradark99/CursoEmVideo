def tabuada(a):
    if a.isdigit:
        a = int(a)
    else:
        print('Digite apenas numero')
    for v in range(11):
        print(v * a)
    return tabuada

numero = input('Digite um numero')
tabuada(numero)