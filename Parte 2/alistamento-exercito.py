from datetime import date
atual = date.today(). year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!.')
elif idade < 18:
    faltam = (18 - idade) + atual
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(18 - idade, faltam))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    