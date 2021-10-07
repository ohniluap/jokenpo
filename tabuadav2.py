print('%'*43)
num = int(input('Digite um número para ver a sua tabuada: '))
print('%'*43)
for tab in range(1, 11):
    print('{} x {:2} = {}'.format(num,tab,  num * tab))
print('%'*43)
