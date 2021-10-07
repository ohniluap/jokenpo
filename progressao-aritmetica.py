t1 = int(input('1º termo: '))
r = int(input('Razão: '))
d = t1 + (10 - 1) * r
for c in range(t1, d + r, r):
    print(c, end=' -> ')
print('FIM')
