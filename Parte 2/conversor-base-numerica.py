num = int(input('Digite um número inteiro: '))
base = int(input('Escolha uma base de conversão:\n [1] Binário\n [2] Octal\n [3] Hexadecimal\n Sua opção: '))
if base == 1:
    bin = format(num, 'b')
    print('{} convertido para Binário é igual a {}.'.format(num, bin))
elif base == 2:
    oct = format(num, 'o')
    print('{} convertido para Octal é igual a {}.'.format(num, oct))
elif base == 3:
    hex = format(num, 'x')
    print('{} convertido para hexadecimal é igual a {}.'.format(num, hex))
    