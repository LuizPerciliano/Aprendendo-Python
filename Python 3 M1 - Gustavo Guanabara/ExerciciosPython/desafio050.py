from datetime import date

print(f"DESAFIO 050 {date.today()}")

soma: int = 0
#lista_inteiros: list[int] = []
lista_inteiros: list = []
for n in range (1,7):
    numero = int(input("Digite 6 números: "))
    lista_inteiros.append(numero)
    if (numero % 2) == 0:
        soma = soma + numero

print(soma)
print(lista_inteiros)
