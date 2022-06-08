desenho = '-.-'*10
cotacao_dolar = 3.27
print(desenho)
print('Programa de cotação')
valor = float(input("Digite quanto você tem na carteira em real: "))
print(f"Seu valor em real de R$ {valor} equivale a U$ {valor*cotacao_dolar} em dollar.")