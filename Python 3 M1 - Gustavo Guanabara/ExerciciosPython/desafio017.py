# o quadrado da hipotenusa é igual a soma do quadrado dos
# catetos(um dos 2 lados do triangulo retangulo)
import math

cat_oposto = float(input("Digite o tamanho do lado do cateto oposto: "))
cat_adjacente = float(input("Digite o tamanho do lado do cateto adjacente: "))
hipotenusa = ((cat_oposto**2) + (cat_adjacente**2)) ** (1/2)
hi = math.hypot(cat_oposto,cat_adjacente)

# usando o teorema de Pitágoras = a2 + b2 = c2
hipotenusa_plus = (pow(cat_oposto,2) + pow(cat_adjacente,2)) ** (1/2)
print(f"A hipotenusa é: {hipotenusa}")
print(f"Hipotenusa bolada {hipotenusa_plus}.")
print(f"A hipotenusa super boladona é {hi:.2f}")

## errei