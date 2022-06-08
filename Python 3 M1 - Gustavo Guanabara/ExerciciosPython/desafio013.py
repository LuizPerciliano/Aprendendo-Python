salario = float(input("Digite seu salário R$ "))
valor_aumento = salario * (15/100)
novo_salario = salario + valor_aumento
print(f"Seu salário atual é R${salario:.2f}, o aumento de 15% em R${valor_aumento:.2f} vai para "
      f"R${novo_salario:.2f}.")