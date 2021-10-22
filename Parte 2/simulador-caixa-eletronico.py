c = 'Caixa Eletrônico'
print('='*40)
print(f'{c:^40}')
print('='*40)
saque = int(input('Valor do Saque R$'))
total = saque
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} de cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
