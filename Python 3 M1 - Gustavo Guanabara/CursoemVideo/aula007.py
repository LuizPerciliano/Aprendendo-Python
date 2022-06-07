''''
nome = input(f"Digite seu nome: ")
print(f"Opi, di boa {nome}?")
print('Opi, di boa {:>20} !'.format(nome))
print('Opi, di boa{:^20}!'.format(nome))
print('Opi, di boa {:=^20}!'.format(nome))
'''
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
soma = int(n1) + int(n2)
multiplicacao = n1*n2
divisao = n1/n2
divisao_inteira = n1//n2
exponenciacao = n1**n2

print(f"A soma é: {soma} \n o produto é {multiplicacao} \n e a divisão é {divisao:.3f} ", end='')
print(f"A divisao inteira é: {divisao_inteira} e a exponenciação é {exponenciacao}")