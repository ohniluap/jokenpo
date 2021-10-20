print('GERADOR DE P.A')
print('-=' * 8)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
termos = termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
