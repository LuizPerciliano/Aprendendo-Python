nome = input("Digite seu nome completo: ").upper().strip()
lista = nome.split()
print(f"Olá {lista[0]} {lista[-1]}")
print(f"último nome {lista[len(lista)-1]}")
