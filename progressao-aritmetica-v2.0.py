print('GERADOR DE P.A')
print('-=' * 8)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = t
d = 1
while d <= 10:
    print('{} -> '.format(t), end='')
    t += r
    d += 1
print('FIM')
