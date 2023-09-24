d = float(input('Qual a distância entre a localização atual e o destino(Km): '))
if d <= 200:
    print('O valor a ser pago pela viagem será de {:.2f} reais.'.format(d*0.5))
else:
    print('O valor a ser pago pela viagem será de {:.2f} reais.'.format(d*0.45))
