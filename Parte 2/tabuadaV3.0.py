num = cont = 0
while True:
    num = int(input('Tabuada de qual valor? '))
    print('-'*25)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num*cont}')
    print('-'*25)
print('Programa tabuada encerrado!')
