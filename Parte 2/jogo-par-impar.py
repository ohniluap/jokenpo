from random import randint
print('=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    par = (jogador + computador) % 2
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}..', end=' ')
    print('DEU PAR' if par == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if par == 0:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break
    if tipo == 'I':
        if par != 0:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break
