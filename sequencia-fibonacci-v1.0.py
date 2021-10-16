print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 36)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    if t3 > t1 and t2:
        t1 = t2
        t2 = t3
        cont += 1
        print(' -> {}'.format(t3), end='')
print('.')
print('~' * 36)
