nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + noota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, média))
if média < 5.0:
    print('O aluno está REPROVADO!')
elif 7.0 > média >= 5.0:
    print('O aluno está em RECUPERAÇÃO!')
elif média >= 7.0:
    print('O aluno está APROVADO!')