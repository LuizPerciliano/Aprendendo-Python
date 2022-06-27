## errei, ao inves de dividir, multipliquei
dict_colors = {
      'red':'\033[0;31m'
      ,'green':'\033[0;32m'
      ,'yellow':'\033[0;33m'
      ,'blue':'\033[1;34m'
      ,'black&white':'\033[0;35;47m'
      ,'close':'\033[m'
}
desenho = '-.-'*10
cotacao_dolar = 4.87 ## cotacao do dia 08/06/2022
cotacao_euro =5.20
print(f"{dict_colors['blue']}{desenho}{dict_colors['close']}")
print(f"{dict_colors['black&white']} Programa de cotação {dict_colors['close']}")
print(f"{dict_colors['blue']}{desenho}{dict_colors['close']}")
valor = float(input("Digite quanto você tem na carteira R$ "))
print(f"Seu valor em real de R$ {dict_colors['yellow']}{valor}{dict_colors['close']} "
      f"equivale a U$ {dict_colors['green']}{valor/cotacao_dolar:.2f}{dict_colors['close']} em dollar "
      f"em euro é E$ {dict_colors['red']}{valor/cotacao_euro:.2f}.{dict_colors['close']}")