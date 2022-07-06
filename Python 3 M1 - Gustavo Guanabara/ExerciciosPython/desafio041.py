from datetime import date

#ano_atual = date.today().year
ano_atual = 2017
ano_nascimento = input("Digite seu ano de nascimento: ")
diferença = ano_atual - float(ano_nascimento)

if diferença <= 9:
    print(f"Mirim")
elif diferença <= 14: #> 9 and diferença <= 14:
    print("Infantil")
elif diferença <=19: #> 14 <= 19:
    print("Junior")
elif diferença <=25:
    print("Sênior")
else:
#elif diferença > 25 :
    print("Master")

print(f"Ano atual {ano_atual}, ano de nascimento {ano_nascimento}, vc tem {diferença:.0f} anos!!!")
