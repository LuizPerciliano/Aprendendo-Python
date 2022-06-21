import random

num_aleatorio = random.randrange(0, 5)
num_digitado = int(input("Qual foi o númer entre 1 e 5 que o computador pensou? "))
if num_aleatorio == num_digitado:
    print(f"Yes, você acertou!")
else:
    print(f"Não! Você digitou {num_digitado} e o PC escolheu {num_aleatorio}!")


