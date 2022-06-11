from math import ceil, sin, cos, tan, radians

angulo = float(input("Digite o angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O angulo {angulo} tem como seno {seno:.2f} "
      f"coseno {cosseno} e tangente {tangente}")

# errei