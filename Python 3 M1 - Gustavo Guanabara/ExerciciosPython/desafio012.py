preco = float(input("Digite o preço do produto R$ "))
novo_preco = preco - (preco * (5/100))
print(f"O preço real é R${preco:.2f}, com desconto fica em R${novo_preco:.2f}.")