# 1 litro pinta 2m2
# se tiver portas e ou janelas, tem q calcular esta e tirar a diferença
# https://blog.meurodape.com/aprenda-a-como-calcular-o-metro-quadrado-de-uma-parede/
# https://industriahoje.com.br/como-calcular-quantidade-de-tinta-por-metro-quadrado
dict_color = {
      'red':'\033[0;31m'
      ,'green':'\033[32m'
      ,'yellow':'\033[33m'
      ,'blue':'\033[0;34m'
      ,'roxo':'\033[0;35m'
      ,'ciano':'\033[36m'
      ,'cinza':'\033[0;37m'
      ,'cinza&ciano':'\033[1;34;47m'
      ,'close':'\033[m'
}
design_pgm = '-.-' * 8
print(f"{dict_color['blue']}{design_pgm}{dict_color['close']}")
print(f"{dict_color['cinza&ciano']} \tDesafio 011 :) !!! \t{dict_color['close']}")
print(f"{dict_color['blue']}{design_pgm}{dict_color['close']}")

largura = float(input(f"{dict_color['yellow']}Digite a largura da parede: {dict_color['close']}"))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
## para tinta, se for 2 demãoes tem que multiplicar pela demão

qtde_tinta = area/2

print(f"A área desta parede é de {dict_color['green']}{area:.1f}m2{dict_color['close']}, "
      f"a quantidade de tinta necessária para pintura será de: {dict_color['green']}{qtde_tinta:.1f}{dict_color['close']} litros.")