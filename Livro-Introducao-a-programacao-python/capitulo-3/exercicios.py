'''
# listagem 3,10
idade = 22
print("[%d]" % idade)
print("[%03d]" % idade)
print("[%3d]" % idade)
print("[%-3d]" % idade) #d para dígitos
print("")
print("%5f" % 5)
print("%5.2f" % 5)

'''
dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)