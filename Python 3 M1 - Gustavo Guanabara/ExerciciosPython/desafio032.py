'''
https://brasilescola.uol.com.br/curiosidades/ano-bissexto.htm
Os anos bissextos foram criados no Império Romano. Eles possuem 366 dias e acontecem em anos divisíveis por quatro, exceto quando terminados em 00.
'''

ano = int(input("Digite um ano: "))
dezena_ano = ano // 1 % 100 # o segundo número é para pegar qtde de dígitos finais
print (f"O ano é {ano} e o final do ano é {dezena_ano}")

if ano % 4 == 0 and dezena_ano != 00:
    print(f" O ano é bissexto.")
else:
    print(f"O ano não é bissexto")
print(f"\n Os anos bissextos foram criados no Império Romano e possuem 366 dias. Acontecem em anos divisíveis por quatro, exceto quando terminados em 00.")
