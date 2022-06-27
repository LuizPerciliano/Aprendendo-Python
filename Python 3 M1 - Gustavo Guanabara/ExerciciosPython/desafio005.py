color_blue = '\033[34m'
color_close = '\033[m'
numero = int(input('Digite um número: '))
print(f"O número digitado é {color_blue}{numero}{color_close} \n seu antecessor é "
      f"{color_blue}{numero - 1}{color_close} \n seu sucessor é {color_blue}{numero + 1}{color_close}.")