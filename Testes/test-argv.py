import sys

n = len(sys.argv)
print("Total de argumentos passados: ", n)
print("\n Nome do script python: ", sys.argv[0])
print("\n Argumentos passados: ", end=" ")

for i in range(1,n):
    print(sys.argv[i], end=" ")

somatorio = 0
for i in range(1, n):
    somatorio += int(sys.argv[i])

print("\n\n Resultado: ", somatorio)