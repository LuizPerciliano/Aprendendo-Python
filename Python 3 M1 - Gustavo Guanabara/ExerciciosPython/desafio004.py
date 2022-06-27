cor_azul = '\033[34m'
cor_red = '\033[31m'
cor_fecha = '\033[m'
cor_pretoebranco = '\033[0;32;40m'
resultado = input('Digite algo: ')
print(f"O tipo digitddo é: {cor_pretoebranco}{type(resultado)}{cor_fecha}")
print(f'{cor_azul}"{resultado}"{cor_fecha} é um número? {cor_red}{resultado.isnumeric()}{cor_fecha}')
print(f"Está em maiúsculo? {cor_red}{resultado.isupper()}{cor_fecha}")
print(f"É alfanumérico? {cor_red}{resultado.isalnum()}{cor_fecha}")