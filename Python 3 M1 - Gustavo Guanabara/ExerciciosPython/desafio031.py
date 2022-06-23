km = float(input("Digite a distância de sua viagem em Km: "))

if km <= 200:
    print(f"Sua viagem custará R${km * 0.50:.2f}")
else:
    print(f"Sua viagem custará R${km  * 0.45:.2f}")