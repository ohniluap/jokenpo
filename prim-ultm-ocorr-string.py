frase = input('Digite uma frase: ').strip().lower()
print('Quantas vezes aparece a letra A: {}'.format(frase.count('a')))
print('Posição que aparece a primeira vez: {}'.format(frase.find('a')+1))
print('Posição que ela aparece a última vez: {}'.format(frase.rfind('a')+1))