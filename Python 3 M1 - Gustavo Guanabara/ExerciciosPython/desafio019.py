'''
import random
nomes_num = 1 2 5 7
random.random(nomes_num)
#random.randint(nomes_num, 1)
'''
# errei
from random import choice

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}!!!")