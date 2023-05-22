diasAlugados = int(input("Quantos dias alugados? "))
kmRodados = float(input("Quantos km rodados? "))
valorTotal = (diasAlugados * 60) + (kmRodados * 0.15)
print("O valor total a pagar é de R$ %.2f" % valorTotal)
