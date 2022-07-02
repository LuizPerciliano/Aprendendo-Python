from datetime import date

ano_atual = date.today().year
ano_nascimento = input("Digite seu ano de nascimento: ")
diferença = ano_atual - float(ano_nascimento)

if diferença <= 9:
    print(f"Mirim")
elif diferença > 9 and diferença <= 14:
    print("Infantil")
elif diferença > 14 and diferença <= 19:
    print("Junior")
elif diferença <=20:
    print("Sênior")
else:
    print("Master")

print(f"Ano atual {ano_atual}, ano de nascimento {ano_nascimento}, vc tem {diferença} anos!!!")
