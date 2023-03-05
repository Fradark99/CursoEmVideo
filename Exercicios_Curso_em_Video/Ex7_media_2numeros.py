def media(a,b):
    if a.isdigit and b.isdigit:
        a = int(a)
        b = int(b)
        soma = (a + b) / 2
        print(soma)
    else:
        print('Digite apenas numero')
    return media

numero = input('Digite um numero')
numero2 = input('Digite um numero')
media(numero, numero2)
