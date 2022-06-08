numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f"O número digitado foi {numero} \n o dobro é {dobro} \n o triplo é {triplo}", end='')
print(f"\n a raiz quadrada é {raiz_quadrada:.2f}.")
print(f"Outra forma de calcular a raiz quadrada {pow(numero,(1/2))}")
