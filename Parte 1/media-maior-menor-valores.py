r = 'S'
num = quant = soma = maior = menor = 0
while r == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = input('Quer continuar? [S/N] ').upper()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
