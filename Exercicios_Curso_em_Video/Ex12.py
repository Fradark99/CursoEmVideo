valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o valor do desconto: "))
desconto = (100 - valorDesconto) / 100

valorFinal = valorProduto * desconto

print("O valor final do produto é: ", valorFinal)