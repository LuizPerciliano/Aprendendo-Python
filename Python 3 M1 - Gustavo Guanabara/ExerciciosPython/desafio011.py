# 1 litro pinta 2m2
# se tiver portas e ou janelas, tem q calcular esta e tirar a diferença
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
qtde_tinta = area*2

print(f"A área desta parede é {area}, a quantidade de tinta necessária para pintura será de: {qtde_tinta}.")