
from datetime import date
from time import sleep

data = date.today().year

print(f"\033[0;35;47m \tDesafio 036 - {data}\t \033[m")

valor_casa = float(input("Digite o valor da casa R$ "))
salario =  float(input("Digite o valor do seu salário R$ "))
anos_pagamento = int(input("Em quantos anos você vai pagar? "))
qtde_parcelas = anos_pagamento * 12
valor_parcela = valor_casa / qtde_parcelas
valor_salario_max = salario * 0.30

if valor_parcela > valor_salario_max:
    print("PROCESSANDO ... \n")
    sleep(2)
    print(f"\033[31mSorry man, você não conseguirá empréstimo com esses dados.\033[m")
else:
    print(f"\033[34mYes man, só pegar, o empréstimo é seu!!!\033[m")
print('\n')
print(f"Serão {qtde_parcelas} parcelas, o valor de cada será R$ {valor_parcela:.2f}!")
print(f"Seu salário é R$ {salario} e sua parcela não pode exceder R$ {valor_salario_max:.2f}.")


