## fazer com string e matemática
numero = input("Digite um número de 0 a 9999: ")
numero_int = int(numero)
print(type(numero))
print(type(numero_int))
print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")

print(numero_int.__sizeof__())
