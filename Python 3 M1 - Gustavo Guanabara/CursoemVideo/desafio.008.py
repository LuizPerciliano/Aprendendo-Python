# errei, coloquei metros como se fossem 60 cm enao coloquei em float
metro = float(input("Digite o metro desejado: "))
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000
decametro = metro / 10
hectometro = metro / 100
km = metro / 1000

print(f" O metro desejado é {metro} \n logo o seu valor em centímetros é: {centimetro} ", end='')
print(f"\n o valor em milímetro é: {milimetro}")

print(f"O kilômetro é {km:.2f} "
      f"O hectômetro é {hectometro:.2f} "
      f"O decâmetro é {decametro} "
      f"O decímetro é {decimetro}.")