cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
nome = input('Digite seu nome = ')
print('É um prazer te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
