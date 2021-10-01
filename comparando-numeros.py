nota1 = int(input('Primeiro número: '))
nota2 = int(input('Segundo número: '))
if nota1 > nota2:
    print('O \033[33mPrimeiro\033[m valor é o maior.')
elif nota2 > nota1:
    print('O \033[33mSegundo\033[m valor é o maior.')
else:
    print('Os dois valores são iguais.')