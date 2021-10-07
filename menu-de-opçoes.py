from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v = 0
while v != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Parar programa''')
    v = int(input('>>> Qual é a sua opção? '))
    if v == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é igual a {}.'.format(v1, v2, soma))
    elif v == 2:
        produto = v1 * v2
        print('O resultado de {} x {} é igual a {}.'.format(v1, v2, produto))
    elif v == 3:
        if v1 > v2:
            maior = v1
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))
        else:
            maior = v2
            print('Entre {} e {} o maior valor é {}.'.format(v1, v2, maior))
    elif v == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif v == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente!')
    print('-='*17)
print('Fim do programa. Volte sempre!')
