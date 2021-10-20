cont = soma = 0
i = int(input('Digite o Início: '))
f = int(input('Digite o Fim: '))
for contagem in range(i, f + 1, 2):
    if contagem % 3 == 0:
        cont += 1
        soma += contagem
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
