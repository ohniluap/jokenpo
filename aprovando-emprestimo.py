casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
if prestação >= 0.3 * s:
    print('Para pagar uma casa de {:.2f} em {} anos, a prestação será de R${:.2f}.\nEMPRÉSTIMO NEGADO!'.format(c, a, p))
else:
    print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}\nEMPRÉSTIMO CONCEDIDO!'.format(c, a, p))