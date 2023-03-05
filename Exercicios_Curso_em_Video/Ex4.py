def dissecando(a):
    print('O tipo de dado é', type(a))
    print('O tipo de dado é', a.isnumeric())
    print('O tipo de dado é', a.islower())
    print('O tipo de dado é', a.isupper())


    return a

frase = input('digite algo')

print(dissecando(frase))

