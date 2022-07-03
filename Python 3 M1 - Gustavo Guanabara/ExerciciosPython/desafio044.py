preco = float(input("Qual o preço normal do produto R$ "))

forma_pagto = int(input("Qual a forma de pagamento: "
                        "1 - Dinheiro / Cheque\n"
                        "2 - A vista no cartão\n"
                        "3 - Em até 2x no cartão\n"
                        "4 - 3x ou mais no cartão\n"
                        ">>> ")) ## ver video aula como implementar isso no input
if forma_pagto == 1:
    print(f"R${preco - (preco * 0.10)}")
elif forma_pagto == 2:
    print(f"R${preco - (preco * 0.05)}")
elif forma_pagto == 3:
    print(f"Preço normal")
elif forma_pagto == 4:
    print(f"R${preco + (preco * 0.20)}")
else:
    print(f"Algo deu trauma")

print(f"O preço normal é R$ {preco} e a forma de pagamento é {forma_pagto}")
