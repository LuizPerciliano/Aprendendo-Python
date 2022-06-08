# 1 litro pinta 2m2
# se tiver portas e ou janelas, tem q calcular esta e tirar a diferença
# https://blog.meurodape.com/aprenda-a-como-calcular-o-metro-quadrado-de-uma-parede/
# https://industriahoje.com.br/como-calcular-quantidade-de-tinta-por-metro-quadrado
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
## para tinta, se for 2 demãoes tem que multiplicar pela demão

qtde_tinta = area/2

print(f"A área desta parede é de {area:.1f}m2, "
      f"a quantidade de tinta necessária para pintura será de: {qtde_tinta:.1f} litros.")