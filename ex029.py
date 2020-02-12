velocidade = int(input('Informe a velocidade do carro: '))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print('O veículo foi multado. O valor da multa é de {:.2f} R$'.format(multa))
else:
    print('')
