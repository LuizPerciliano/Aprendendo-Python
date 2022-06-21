frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A palavra 'A' aparece pela primeira vez na posição {frase.find('A')+1},")
print(f"pela última vez na posição {frase.rfind('A')+1}")
print(f"O total de letras 'A' são {frase.count('A')} vez(es).")
