from random import randint
from time import sleep

pc = randint(0,2)
itens = ('Pedra','Papel','Tesoura')
errou = 'Putz, jogada inválida'

print("JOKENPO")
opcao = int(input('''
    Digite sua opção:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    >>> 
'''))

print("JO ...")
sleep(1)
print("KEN ...")
sleep(1)
print("PÔ!!!")
sleep(1)

if opcao == 0:
    if pc == 0:
        print("EMPATE")
    elif pc == 1:
        print("LOOSE")
    elif pc == 2:
        print("WIN")
    else:
        print({errou})

elif opcao == 1:
    if pc == 0:
        print("WINN")
    elif pc == 1:
        print("EMPATEE")
    elif pc == 2:
        print("LOOSE")
    else:
        print({errou})

elif opcao == 2:
    if pc == 0:
        print("LOOOSE")
    elif pc == 1:
        print("GANHOuuu")
    elif pc == 2:
        print("EMPATEEEEE")
    else:
        print({errou})

print(f"Você escolheu {opcao} e o PC {pc}!")
print(f"Você escolheu {itens[opcao]} e o Computador {itens[pc]}")