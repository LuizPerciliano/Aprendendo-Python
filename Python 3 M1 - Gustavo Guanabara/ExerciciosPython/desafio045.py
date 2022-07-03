## Jokenpô - Jogo papel e tesoura - desafio 045
## tratar para digitar somente entre os números
'''
a tesoura corta o papel, mas quebra com a pedra; o papel embrulha a pedra, mas é cortado pela tesoura e a pedra quebra a tesoura e é embrulhada pelo papel.
https://buzzfeed.com.br/quiz/vamos-jogar-jokenpo#:~:text=Caso%20voc%C3%AA%20n%C3%A3o%20saiba%2C%20jokenp%C3%B4,entre%20pedra%2C%20papel%20e%20tesoura.&text=E%20funciona%20assim%3A%20a%20tesoura,e%20%C3%A9%20embrulhada%20pelo%20papel.
'''
import random

opi = int(input("Digite:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n >>> "))
pc = random.randint(1,3)

if opi == 1 and pc == 1:
    print(f"Ambos pedra - empate")
elif opi == 1 and pc == 2:
    print(f"A pedra é embrulhada pelo papel, YOU LOSE!!!")
elif opi ==1 and pc == 3:
    print("A pedra quebra a tesoura, YOU WIN!!!")
else:
    print("Vamos tentar novamente!!!")

print(f"Você digitou {opi}, o computador {pc}")