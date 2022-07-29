from datetime import date

ano_atual = date.today()
menu_1 = '-.-' * 20

dict_collor = {
    'red':'\033[0;31m'
    ,'green':'\033[0;32m'
    ,'yellow':'\033[0;33m'
    ,'gray-ciano':'\033[1;36;47m'
    ,'close':'\033[m'
}

print(f"{dict_collor['yellow']}{menu_1}")
print(f"{dict_collor['gray-ciano']}DESAFIO 049 - TABUADA NO LAÇO - {ano_atual}!!!{dict_collor['close']}")
print(f"{dict_collor['yellow']} {menu_1}{dict_collor['close']}")

numero = int(input("Digite um número para gerar a tabuada: "))
for n in range(1,11):
    print(f"{n} * {numero} = {n * numero}")