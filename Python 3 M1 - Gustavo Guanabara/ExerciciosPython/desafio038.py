
try:
    num1 = int(input("Digite o primeiro inteiro: "))
    num2 = int(input("Digite o segundo inteiro: "))

    if num1 > num2:
        print(f"O primeiro valor é maior")
    elif num2 > num1:
        print(f"O segundo valor é maior")
    else:
        print(f"Putz, ambos são iguais!!!")
except ValueError:
    print("Putz, valor digitado é inválido!!!")
