print("\33[1;31;43mOpi, mundo!\033[m") ## modo 1 de usar cores

nome = 'Perciliano'
cor_abre = '\033[4;34m'
cor_fecha = '\033[m'
dict_cores = {'limpa':'\033[m',
              'azul':'\033[34m',
              'amarelo':'\033[33m',
              'pretoebranco':'\033[7;30m'

}

print(f"Opi, muito prazer em te conhecer {cor_abre}{nome}{cor_fecha}!!!") ## modo 2 de usar cores

print(f"Opi {dict_cores['pretoebranco']}{nome}{dict_cores['limpa']} sup!!!") ## modo 3 de usar cores