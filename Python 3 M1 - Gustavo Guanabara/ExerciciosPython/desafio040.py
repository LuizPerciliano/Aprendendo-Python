nota_1 = input("Digite a nota 1: ")
nota_2 = input("Digite a nota 2: ")

media = (float(nota_1) + float(nota_2)) / 2
if media < 5:
    print("Reprovado!")
elif media > 5 and media < 6.9:
    print("Recuperação")
elif media >=7:
    print("Uhuuuuuuu, passou!!!")
else:
    print("Algo deu errado")

print(f"{media}")