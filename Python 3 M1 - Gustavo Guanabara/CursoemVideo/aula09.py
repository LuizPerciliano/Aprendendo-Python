frase = "Curso em Vídeo Python"
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print("Curso" in frase)
print(frase.find("Curso")) # achado e inicia na posição 9
print(frase.lower().find("vídeo"))

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
