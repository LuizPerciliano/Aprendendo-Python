#https://www.programasaudefacil.com.br/calculadora-de-imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc > 25 and imc < 30 :
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("obesidade")
else:
    print("Putz, obesidade mórbida!!!")


print(f"Sua altura é {altura}, seu peso é {peso}, seu IMC é {imc}!")

