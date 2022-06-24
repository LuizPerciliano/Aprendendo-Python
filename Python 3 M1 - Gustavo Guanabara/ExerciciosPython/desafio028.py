import random
from random import randint
from time import sleep
from timeit import timeit

num_aleatorio = random.randrange(0, 5)
print(num_aleatorio)

computador = randint(0, 5)
print(computador)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
num_digitado = int(input("Qual foi o númer entre 1 e 5 que o computador pensou? "))
print(f"PROCESSANDO ... ")
sleep(2)
if computador == num_digitado:
    print(f"Yes, você acertou!")
else:
    print(f"Não! Você digitou {num_digitado} e o PC escolheu {num_aleatorio}!")


