num = 0 
soma = 0
total = 0
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    total += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(total, soma))
