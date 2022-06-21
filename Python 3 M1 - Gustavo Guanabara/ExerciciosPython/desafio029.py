velocidade = float(input("Digite a velocidade do carro em Km/h: "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(f"Você está dentro do limite de velocidade.")
else:
    print(f"Você ultrapassou em {(velocidade - 80):.1f} Km/h, sua multa será de R${multa:.2f}")