nome = str(input('Digite uma frase: ')).lower()
print('A letra "a" aparece {} vezes na frase.'.format(nome.count('a')))
print('A primeira letra "a" aparece na posição: ', nome.find('a')+1)
print('A última letra "a" aparece na posição: ', nome.rfind('a') + 1)