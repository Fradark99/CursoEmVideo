catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
