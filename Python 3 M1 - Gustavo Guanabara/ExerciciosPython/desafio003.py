cor_azul_abre = '\033[34m'
cor_fecha = '\033[m'

numero1 = input(f"Digite o primeiro número: ")
numero2 = input(f"Digite o segundo número: ")
soma = int(numero1) + int(numero2)
print(f"A soma de {cor_azul_abre}{numero1}{cor_fecha} e {cor_azul_abre}{numero2}{cor_fecha} é igual a {soma}!")
