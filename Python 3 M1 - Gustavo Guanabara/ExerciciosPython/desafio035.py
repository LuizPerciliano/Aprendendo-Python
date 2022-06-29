# errei
'''
https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-a-condicao-existencia-um-triangulo.htm#:~:text=N%C3%A3o%20%C3%A9%20necess%C3%A1rio%20fazer%20as,maior)%20ter%C3%A1%20o%20mesmo%20resultado.

Condição de existência de um triângulo
Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
Por exemplo, dados os segmentos AB = 16 cm, CD = 20 cm e EF = 30 cm, é possível usá-los para construir um triângulo, pois as somas abaixo são verdadeiras:
16 + 20 = 36 > 30
16 + 30 = 46 > 20
30 + 20 = 50 > 16

5, 1 e 2 nao rola

'''

reta_1 = float(input("Digite a reta 1: "))
reta_2 = float(input("Digite a reta 2: "))
reta_3 = float(input("Digite a reta 3: "))
'''
if reta_1 + reta_2 > reta_3:
    print(f" Com os valores informados, é possível formar um triangulo!")
elif reta_2 + reta_3 > reta_1:
    print("Tbm é possível")
else:
    print("Não forma um triangulo")
'''
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print(f"Rola um triângulo!!!")
else:
    print("Não rola um triângulo!!!")







