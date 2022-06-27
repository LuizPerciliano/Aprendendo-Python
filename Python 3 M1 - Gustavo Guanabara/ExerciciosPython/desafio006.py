color_blue = '\033[34m'
color_green = '\033[32m'
color_close = '\033[m'

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f"O número digitado foi {color_blue}{numero}{color_close} \n o dobro é {dobro} \n o triplo é {triplo}", end='')
print(f"\n a raiz quadrada é {raiz_quadrada:.2f}.")
print(f"Outra forma de calcular a  \033[7;30;41m raiz quadrada {color_close} {pow(numero,(1/2))}")
