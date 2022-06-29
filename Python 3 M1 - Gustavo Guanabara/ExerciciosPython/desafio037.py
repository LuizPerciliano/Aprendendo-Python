from datetime import date
from time import sleep

dict_colors = {
    'red':'\033[31m'
    ,'blue_':'\033[1;34m'
    ,'gray&purple':'\033[1;35;47m'
    ,'close':'\033[m'
}
desenho = '=.=' * 12
print(f"{dict_colors['blue_']}{desenho}{dict_colors['close']}")
print(f" \t {dict_colors['gray&purple']} Desafio 037 - Ano {date.today().year}{dict_colors['close']} \t")
print(f"{dict_colors['blue_']}{desenho}{dict_colors['close']}")

numero = int(input("Digite um número inteiro para a conversão: "))
num_conversao = int(input("Digite: \n1 para binário \n2 para octal \n3 para hexadecimal "))
if num_conversao == 1:
    print("PROCESSANDO ...")
    sleep(2)
    print(f"O número {numero} convertido para binário é {numero + num_conversao}")
else:
    print(f"Vamos continuar tentando...")
