distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))
valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem vai custar R${:.2f}.'.format(valor))