from datetime import date
dict_color = {
    'red':'\033[31m'
    ,'blue':'\033[34m'
    ,'gray&purple':'\033[0;35;47m'
    ,'close':'\033[m'
}
desenho = '=.=' * 8
ano_atual = date.today().year
print(f"{dict_color['blue']}{desenho}{dict_color['close']}")
print(f"{dict_color['gray&purple']} \tAula 08 - {ano_atual}\t {dict_color['close']}")
print(f"{dict_color['blue']}{desenho}{dict_color['close']}")

nome = str(input("Digite seu nome: ")).strip().upper()
if nome == 'PERCILIANO':
    print(f"Que nome lindo!!!")
elif nome == 'LUIZ' or nome == 'MARIA' or nome == 'PEDRO':
    print(f"Seu nome é bem popular no Brasil!!!")
elif nome in 'ANA CLÁUDIA LUCIANA':
    print(f"Belo nome feminino!!!")
else:
    print(f"Seu nome é bem normal!!!")
print(f"{dict_color['blue']}Seu nome é: {nome}{dict_color['close']}")