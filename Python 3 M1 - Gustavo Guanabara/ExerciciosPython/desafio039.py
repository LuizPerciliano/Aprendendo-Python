## reimplementar desafio 039 perguntando antes se é homem ou mulher e calcular só qd for mulher
from datetime import date

try:
    #ano_atual = date.today().year
    ano_atual = 2017
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade == 18: # 2004
        print(f"Você está na hora de se alistar, foi?")
    elif ano_atual - ano_nascimento > 18:
        print(f"Passou {(ano_atual - ano_nascimento) - 18} anos do alistamento, vai ter que pagar uma multa!") # 1978
        print(f"Seu alistamente foi em {ano_nascimento + 18}")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Ainda não chegou seu tempo, vai demorar {saldo} ano(s)!!")
        ano = ano_atual + saldo
        #print(f"Seu ano de alistamente será em {ano_nascimento + 18}")
        print(f"Seu ano de alistamento será em {ano}.")
except ValueError:
    print(f"Putz, valor digitado inválido")

print(f"Quem nasceu em {ano_nascimento} tem ou vai fazer {idade} anos de idade em {ano_atual}!!!")