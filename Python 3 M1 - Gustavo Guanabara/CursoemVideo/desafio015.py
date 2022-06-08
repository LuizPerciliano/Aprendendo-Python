km_percorrido = float(input("Digite a quantidade de kilômetro percorrido: "))
dias_aluguel = int(input("Digite a quantidade de dias alugado: "))
custo_dia = 60
valor_km_rodado = 0.15
preco_aluguel = (custo_dia * dias_aluguel) + (km_percorrido * valor_km_rodado)
print(f"Você rodou {km_percorrido} por {dias_aluguel:.0f} dias, logo, deve R${preco_aluguel:.2f}")
