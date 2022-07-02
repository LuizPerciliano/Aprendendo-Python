from datetime import date

try:
    ano_atual = date.today().year
    ano_nascimento = int(input("Digite seu ano de nascimento: "))

    if ano_atual - ano_nascimento == 18: # 2004
        print(f"Você está na hora de se alistar, foi?")
    elif ano_atual - ano_nascimento > 18:
        print(f"Passou {(ano_atual - ano_nascimento) - 18} anos de alistamento, vai ter que pagar uma multa!") # 1978
    elif ano_atual - ano_nascimento < 18:
        print(f"Ainda não chegou seu tempo, vai demorar {(ano_atual - ano_nascimento) + 18} anos!!")
#    print(f"O ano atual é {ano_atual}")

except ValueError:
    print(f"Putz, valor digitado inválido")
