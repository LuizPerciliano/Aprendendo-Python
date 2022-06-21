'''
nome = str(input("Qual o seu nome: "))
if nome == 'Luiz':
    print('Que nome lindo você tem!')
else:
    print("Seu nome é tão normal chuchu!")
print(f"Bom dia, {nome}!")
'''

n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
m = (float(n1) + float(n2)) / 2
print(f"A média foi de {m:.1f}")
if m >= 6:
    print(f"Sua média foi boa, CONGRATULATIONS!!!")
else:
    print(f"Ih, estuda + heim, tá tenso!!!")
