from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') # Faz o computador imprimir um número aleatório
print('-=-'* 20)
jogador = int(input('Em qual número eu pensei? ')) # Jogador tenta adivinhar
print('{}PROCESSANDO...'.format('\033[36m', '\033[m'))
sleep(2)
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('Você perdeu!\nEu pensei no número {} e não no {}.'.format(computador, jogador))