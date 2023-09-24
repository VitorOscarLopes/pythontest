kmh = float(input('Qual a velocidade do carro: '))
multa = (kmh - 80) * 7

if kmh > 80:
    print('Você excedeu a velocidade limite imposta pelo DETRAN(80 Km/h) em {:.1f}Km/h. Sua multa será de {:.2f} reais.'.format
          ((kmh-80), multa))
else:
    print('Você estava andando dentro da velocidade limite(80 Km/h) e não será multado.')
