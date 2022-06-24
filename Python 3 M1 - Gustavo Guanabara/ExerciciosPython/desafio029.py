velocidade = float(input("Digite a velocidade do carro em Km/h: "))
multa = (velocidade - 80) * 7
if velocidade >= 80: # estrutura de condição simples, só um if sem else
    print(f"Você ultrapassou em {(velocidade - 80):.1f} Km/h, sua multa será de R${multa:.2f}")
print(f"Tenha um bom dia! Dirija com segurança!.")