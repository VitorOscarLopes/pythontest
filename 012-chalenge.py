house = float(input('Quanto custa a casa: '))
sal = float(input('Qual seu salário: '))
year = int(input('Em quantos anos deseja pagar sua casa: '))
pag = sal * 0.3
men = house / (year * 12)
if pag >= men:
    print('Você pode comprar essa casa. E o valor mensal a ser pago será de R${:.2f}'.format(men))
else:
    print('Não é recomendável que você compre essa casa.')
