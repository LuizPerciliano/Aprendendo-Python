## fazer com string e matemática
numero = input("Digite um número de 0 a 9999: ")
numero_int = int(numero)
unidade = numero_int // 1 % 10 ## pega só um dígito 100 pega 2
dezena = numero_int // 10 % 10
centena = numero_int // 100 % 10
milhar = numero_int // 1000 % 10
print(type(numero))
print(type(numero_int))
'''print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}") '''

print(f"Unidade: {unidade}")
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f"Milhar: {milhar}")