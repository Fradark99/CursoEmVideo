nome = input("Digite seu nome: ")
print("Codificando seu nome...")

print(f"Seu nome maiusculo: {nome.upper()}")
print(f"Seu nome minusculo: {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")
