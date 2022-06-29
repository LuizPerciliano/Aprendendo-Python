'''
https://brasilescola.uol.com.br/curiosidades/ano-bissexto.htm
Os anos bissextos foram criados no Império Romano. Eles possuem 366 dias e acontecem em anos divisíveis por quatro, exceto quando terminados em 00.
'''
from datetime import date
ano = int(input("\033[33mDigite o ano que deseja analisar ou 0 para o ano atual: \033[m"))
dezena_ano = ano // 1 % 100 # o segundo número é para pegar qtde de dígitos finais
print (f"O ano é {ano} e o final do ano é {dezena_ano}")

#if ano % 4 == 0 and dezena_ano != 00: # meinha resoluçao, correta
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f" O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto")
print(f"\n Os anos bissextos foram criados no Império Romano e possuem 366 dias. Acontecem em anos divisíveis por quatro, exceto quando terminados em 00.")
