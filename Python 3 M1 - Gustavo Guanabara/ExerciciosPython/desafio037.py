# depois de ver a solucão, tentar implementar com match
    # https://docs.python.org/3/tutorial/controlflow.html#match-statements

#Aula extra de “Notação Posicional - Bases Numéricas”
# https://youtu.be/J5q7s7l2EuI?list=PLHz_AreHm4dlmeSpWzJGWOmFnVF5k_IYi

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
num_conversao = int(input('''Escolha uma das bases para conversão:
    [ 1 ] para binário
    [ 2 ] para octal
    [ 3 ] para hexadecimal 
    >>> '''))
if num_conversao == 1:
    print("PROCESSANDO ...")
    sleep(2)
    print(f"O número {numero} convertido para binário é {bin(numero)[2:]}") ## tem uma explicacao muito boa do LAcerda dos Canetas Pretas
elif num_conversao == 2:
    print(f"O número {numero} convertido para octal é {oct(numero)[2:]} ")
elif num_conversao == 3:
    print(f"O número {numero} convertido para hexadecimal é {hex(numero)[2:]} ")
else:
    print(f"Vamos continuar tentando...")
