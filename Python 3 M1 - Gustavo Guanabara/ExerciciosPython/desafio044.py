print('{:=^40}'.format(' LOJAS PERCILIANO '))

preco = float(input("Qual o preço normal do produto R$ "))

forma_pagto = int(input('''Qual a forma de pagamento:
                        1 - Dinheiro / Cheque
                        2 - A vista no cartão
                        3 - Em até 2x no cartão
                        4 - 3x ou mais no cartão
                        ">>> ''')) ## ver video aula como implementar isso no input

if forma_pagto == 1:
    total = preco - (preco * 10 / 100)
elif forma_pagto == 2:
    total = preco - (preco * 0.05)
elif forma_pagto == 3:
    total = preco
    print(f"Você pagará 2 parcelas no valor de R${total / 2} SEM JUROS")
elif forma_pagto == 4:
    parcelas = int(input("Digite em quantas parcelas será: "))
    total = preco + (preco * 0.20)
    print(f" O valor total ficou em R${total}, divido em {parcelas} de R$ {total / parcelas} COM JUROS")
else:
    total = preco
    print(f"Algo deu trauma")

print(f"O preço normal é R${preco}, o total ficou em R${total} e a forma de pagamento foi {forma_pagto}")
