def medida(a):
    if a.isdigit:
        a = int(a)
        metros = a
        km = a / 1000
        cm = a/10000
        mm = a/ 100000
        print(
            f'A medida em metros é {metros}', '\n'
            f'A medida em Kilometros é {km}', '\n'
            f'A medida em centimetros é {cm}', '\n'
            f'A medida em milimetros é {mm}'  )
    else:
        print('Digite apenas numero')
    return medida

numero = input('Digite um numero')
medida(numero)