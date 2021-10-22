totH = tot18 = totM20 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*25)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        print('-'*25)
        break
print(f'Pessoas com mais de 18: {tot18}')
print(f'Homens cadastrados: {totH}')
print(f'Mulheres com menos de 20 anos: {totM20}')
