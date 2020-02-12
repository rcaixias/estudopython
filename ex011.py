at = float(input('Qual é a altura da parede? '))
lg = float(input('Qual é a largura da parede? '))
mq = at * lg
lt = mq / 2
print('Sua parede tem {}m² e precisa de {} litros de tinta para pinta-la.'.format(mq, lt))