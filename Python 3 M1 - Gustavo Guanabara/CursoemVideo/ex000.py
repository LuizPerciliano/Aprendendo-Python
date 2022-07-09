'''
Veja o resumo da regra abaixo:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

print('Olá, mundo!')

a = 4
b = 40
c = 5

if abs(a - b) < c < a + b and abs(a - c) < b < a + c and abs(b - c) < a < b + c:
    print('é triangulo')
else:
    print('deu ruim')




