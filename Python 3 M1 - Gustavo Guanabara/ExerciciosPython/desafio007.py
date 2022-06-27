dict_colors = {
    'red':'\033[0;31m',
    'green':'\033[0;32m',
    'blue':'\033[0;34m',
    'close':'\033[m',
}
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2

print(f"As notas foram {dict_colors['green']}{nota1}{dict_colors['close']} e {dict_colors['green']}{nota2}{dict_colors['close']}. "
      f"A média foi {dict_colors['red']}{media:=^10}{dict_colors['red']}{dict_colors['close']}.")
print(f"As notas foram {nota1} e {nota2}. A média foi {media:.1f}.")