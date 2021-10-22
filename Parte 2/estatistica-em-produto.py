loja = 'loja '.upper()
print('-'*25)
print(f'{loja:^25}')
total = totmil = menorvalor = cont =  0
barato = ''
while True:
    print('-'*25)
    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menorvalor:
        menorvalor = valor
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total da compra: R${total:.2f}')
print(f'{totmil} Produto custando mais de R$1.000')
print(f'Produto mais barato foi {barato} que custou R${menorvalor:.2f}')
