valor = int(input('Preço das compras R$: '))
print('FORMAS DE PAGAMENTO')
opção = int(input('[1] à vista no dinheiro/cheque\n[2] à vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nOpção: '))
if opção == 1:
    desconto = valor * 0.1
    valornovo = valor - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valornovo))
elif opção == 2:
    desconto = valor * 0.05
    valornovo = valor - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valornovo))
elif opção == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(valor / 2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor))
elif opção == 4:
    numparcela = int(input('Quantas parcelas? '))
    parcela = valor / numparcela + (valor / numparcela * 0.2)
    valornovo = valor + (valor * 0.2)
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS.'.format(numparcela, parcela))
    print('A compra de R${:.2f} vai custar {:.2f} no final.'.format(valor, valornovo))
else:
    print('OPÇÃO INVÁLIDA, Tente novamente!')
    