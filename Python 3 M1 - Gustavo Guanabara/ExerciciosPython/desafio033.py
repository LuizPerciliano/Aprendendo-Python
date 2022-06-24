num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

lista = num1, num2, num3
lista = sorted(lista, reverse=False)
print(lista)
print(f"O menor número é {lista[0]} e o maior {lista[-1]}")

if num1 < num2 and num2 < num3:
    print(f"O menor número é {num1}")
elif num2 < num1 and num1 < num3:
        print(f"{num2} é o menor número")
else:
    print(f"{num3} é o menor número")