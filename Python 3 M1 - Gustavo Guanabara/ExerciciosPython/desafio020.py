import random

a1 = str(input("Digite o primeiro aluno: "))
a2 = str(input("Digite o segundo aluno: "))
a3 = str(input("Digite o terceiro aluno: "))
a4 = str(input("Digite o quarto aluno: "))
lista_alunos = [a1, a2, a3, a4]
random.shuffle(lista_alunos)

print(f"A ordem de apresentação dos alunos será {lista_alunos}.")

# errei