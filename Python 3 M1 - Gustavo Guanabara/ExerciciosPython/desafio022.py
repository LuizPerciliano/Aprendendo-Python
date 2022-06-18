nome = str(input("Digite seu nome completo: ").upper().strip())
qtd_espaco = nome.count(' ')

print(f"Seu nome é {nome} e em minúsculo é {nome.lower()}")
print(f"Quantidade de caracteres totais é {len(nome)}, existe(m) {qtd_espaco} caracter(es) em branco")
print(f"Quantidade de caracteres totais sem espaços é {len(nome) - qtd_espaco} ")
nome_dividido = nome.split()
print(nome_dividido)
print(f"O primeiro nome {nome_dividido[0]} tem {len(nome_dividido[0])} caracateres.")
