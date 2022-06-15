'''
qtd_cigarros = input("Digite a quantidade de cigarros fumados por dia: ")
anos_fumante = input("Quantos anos tem de fumante: ")
anos_minutos = int(anos_fumante) / 525600 # valor de um ano em minutos
tempo_min_fumado_dia = 0 #qtd_cigarros *

vida_minutos_cigarro = 0
dias_vida_faltante = 0

print(f"Tempo de fumante em minutos {anos_minutos}.")
'''
##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2022
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 03\exercicio-03-15.py
##############################################################################

cigarros_por_dia = int(input("Quantidade de cigarros por dia:"))
anos_fumando = float(input("Quantidade de anos fumando:"))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
print("Redução do tempo de vida %8.2f dias." % redução_em_dias)