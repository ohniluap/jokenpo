tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('carro velho')
print('----Fim----')

# Condição simplificada

tempo = int(input('Quantos anos tem seu carro'))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('----FIM----')