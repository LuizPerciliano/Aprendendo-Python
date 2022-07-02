# Complementar do desafio 035

segmento1 = int(input("Digite o segmento de reta 1: "))
segmento2 = int(input("Digite o segmento de reta 2: "))
segmento3 = int(input("Digite o segmento de reta 3: "))

if segmento1 == segmento2 and segmento1 == segmento3:
    print("Equilátero")
elif segmento1 == segmento2 or segmento2 == segmento3:
    print("Isóceles")
elif segmento1 != segmento2 or segmento2 != segmento3:
    print("Escaleno")



print(f"Segemento 1 -  {segmento1}\nSegmento 2 - {segmento2}\nSegmento 3 - {segmento3}")

