cidade = input("Digite uma cidade: ").lower().strip()
lista = cidade.split()
print(lista)
print(f"Essa cidade começa com a palavra 'Santo'? {lista[0] == 'santo'}")
print(f"Ihhh {cidade[:5] == 'santo' }")
print(f"{cidade.find('santo')}")