qd = float(input('Quantos dias o carro ficou alugado? '))
kr = float(input('Quantos km foram rodados? '))
preço = qd * 60 + kr * 0.15
print('O valor a ser pago é de {:.2f} R$'.format(preço))