'''
from math import floor, sqrt

# ceil arredonda para cima
#
num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raiz quadrada de {num} é {floor(raiz)}.")
'''

import random
import emoji
#num = random.random() # gera números aleatórios entre 0 e 1
num = random.randint(1, 10) # gera números aleatórios entre 0 e 1
print(num)
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.emojize(":smile:", language='alias'))
print(emoji.emojize(":neckbeard:", language='alias'))

