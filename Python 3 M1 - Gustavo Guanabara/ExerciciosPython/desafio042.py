# Complementar do desafio 035
from datetime import date
from time import sleep

ano_atual = date.today().year
menu1 = '=.=' * 18
menu2 = '-.-' * 5

dict_cores = {
    'red':'\033[31m'
    ,'blue':'\033[0;34m'
    ,'gray&purple':'\033[7;37;45m'
    ,'close':'\033[m'
}

print(dict_cores['blue'],menu1, dict_cores['close'])
print (f"{dict_cores['gray&purple']}{menu2} DESAFIO 042 - {ano_atual} {menu2}{dict_cores['close']}")
print(dict_cores['blue'],menu1,dict_cores['close'])

segmento1 = float(input("Digite o segmento de reta 1: "))
segmento2 = float(input("Digite o segmento de reta 2: "))
segmento3 = float(input("Digite o segmento de reta 3: "))
msg = 'Os segmentos digitados podem formar um triângulo'

if abs(segmento1 - segmento2) < segmento3 < segmento1 + segmento2 and abs(segmento1 - segmento3) < segmento2 < segmento1 + segmento3 and abs(segmento2 - segmento3) < segmento1 < segmento2 + segmento3:
    print(f"{dict_cores['blue']}Processando ... {dict_cores['close']}")
    sleep(2)
    if segmento1 == segmento2 == segmento3:
        print(f"{msg} EQUILÁTERO - (Todos os lados são iguais!)")
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print(f"{msg} ESCALENO - Todos os lados são distintos!")
    #elif segmento1 != segmento2 or segmento2 != segmento3:
    else:
        print(f"{msg} ISÓSCELES - Dois lados são iguais!")
else:
    print("Não é possível formar um triângulo!!!")

print(f"Segemento 1 -  {segmento1}\nSegmento 2 - {segmento2}\nSegmento 3 - {segmento3}")

