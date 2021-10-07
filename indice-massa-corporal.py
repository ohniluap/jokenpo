peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura ** 2
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso normal!')
elif imc < 25:
    print('Você está no Peso ideal!')
elif imc < 30:
    print('Você está no Sobrepeso!')
elif imc < 40:
    print('Você está em Obesidade!')
else:
    print('Você está em Obesidade Mórbida, cuidado!')
    