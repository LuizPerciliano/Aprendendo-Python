km = float(input("Digite a distância de sua viagem em Km: "))
'''
if km <= 200:
    print(f"Sua viagem custará R${km * 0.50:.2f}")
else:
    print(f"Sua viagem custará R${km  * 0.45:.2f}")
'''
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f"O preço da sua passagem será de \033[34mR$ {preco}")