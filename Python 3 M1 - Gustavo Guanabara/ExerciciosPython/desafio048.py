''''
https://escolakids.uol.com.br/matematica/multiplos-de-um-numero.htm
Para determinar os múltiplos de um número inteiro n, devemos multiplicar esse número por outros números inteiros,
os resultados dessa operação são os múltiplos de n. Podemos escrevê-los utilizando uma fórmula geral, veja:

Para determinar os múltiplos do número 2, devemos multiplicá-lo por números inteiros, nesse exemplo vamos encontrar os 11 primeiros múltiplos de 2.
A fim de facilitar, estabeleceremos uma notação para os múltiplos de um número, em vez de montar uma tabuada. Vamos escrevê-los assim:

M (2) = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, ...}

Vídeo time 28:27
'''

soma = 0
for c in range(1,7, 2):
    for c2 in c:
        c2 * c
        soma = soma + c
        print(c)
print(soma)
