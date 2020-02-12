from random import randrange
x = int(input('Digite um número de 1 a 5: '))
if randrange(1, 5) == x:
    print('Você acertou')
else:
    print('Número errado')