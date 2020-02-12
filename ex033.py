num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('informe o terceiro número: '))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num1 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('Maior {:.0f}'.format(maior))
print('Menor {:.0f}'.format(menor))