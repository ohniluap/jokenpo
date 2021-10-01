from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))

# Condição Simplificada

from math import pow
oposto = float(input('Cateto Oposto: '))
adjacente = float(input('Cateto Adjacente: '))
hipotenusa = pow(opt, 2) + pow(adj, 2)
print('O quadrado da hipotenusa é igual a {:.2f}.'.format(math.sqrt(hipotenusa)))
