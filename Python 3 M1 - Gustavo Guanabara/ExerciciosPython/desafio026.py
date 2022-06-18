frase = input("Digite uma frase: ")
print(f"A palavra 'A' aparece pela primeira vez na posição {frase.find('A')},"
      f"Aparece pela última vez na posição {frase.find('A') - 1}"
      f"O total de letras 'A' são {frase.count('A')} vez(es).")
