from math import hypot
catetoadj = float(input('Informe o valor do cateto adjacente: '))
catetoopo = float(input('Informe o valor do cateto oposto: '))
hipotenusa = hypot(catetoadj, catetoopo)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))