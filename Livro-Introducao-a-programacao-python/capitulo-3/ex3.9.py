nome = str(input("Digite seu nome: "))
dias = input("Digite a quantidade de dias: ")
horas = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
segundos = input("Digite a quantidade de segundos: ")
segundos_total = (int(segundos) * 1)
minutos_total = (int(minutos) * 60)
horas_total = (int(horas) * 3600)
dias_total = int(dias) * 86400 # Um dia tem 24 horas, logo 24 * 3600 segundos
total_segundos_geral = segundos_total + minutos_total + horas_total + dias_total
print(f"{str.upper(nome)}, a quantidade de segundos total é {total_segundos_geral}.")