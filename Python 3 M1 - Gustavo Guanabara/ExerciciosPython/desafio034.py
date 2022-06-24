salario = float(input("Digite seu salário R$ "))
texto_padrao = 'Seu novo salário será de R$'

if salario < 1250:
    print(f"{texto_padrao} {salario + (salario * 0.10):.2f}")
else:
    print(f"{texto_padrao} {salario + (salario * 0.15):.2f}")
