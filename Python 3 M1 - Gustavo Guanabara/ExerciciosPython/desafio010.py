## errei, ao inves de dividir, multipliquei
desenho = '-.-'*10
cotacao_dolar = 4.87 ## cotacao do dia 08/06/2022
cotacao_euro =5.20
print(desenho)
print('Programa de cotação')
valor = float(input("Digite quanto você tem na carteira R$ "))
print(f"Seu valor em real de R$ {valor} "
      f"equivale a U$ {valor/cotacao_dolar:.2f} em dollar "
      f"em euro é E$ {valor/cotacao_euro:.2f}.")