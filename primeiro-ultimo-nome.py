nomecompleto = str(input('Escreva seu nome completo: ')).strip().lower()
nome = nomecompleto.split()
print('Primeiro Nome: {}'.format(nome[0]))
print('Último Nome: {}'.format(nome[len(nome)-1]))
