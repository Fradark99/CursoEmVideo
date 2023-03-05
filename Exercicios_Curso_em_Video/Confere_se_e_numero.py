def eNumero(*args):
    numeros = []
    for v in args:
        if v.isdigit():
            numeros.append(int(v))
        else:
            print('Um ou mais numeros não estão corretos')
    return numeros
 



