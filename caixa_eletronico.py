print('='*40)
print('{:^40}'.format('BANCO DEV'))
print('='*40)
saque = int(input('Quanto deseja sacar: '))
n100 = saque // 100
n50 = saque % 100 // 50
n20 = saque % 100 % 50 // 20
n10 = saque % 100 % 50 % 20 // 10
n1 = saque % 100 % 50 % 20 % 10 // 1
if n100 > 0:
    print(f'Total de {n100} cédulas de R$ 100')
if n50 > 0:
    print(f'Total de {n50} cédulas de R$ 50')
if n20 > 0:
    print(f'Total de {n20} cédulas de R$ 20')
if n10 > 0:
    print(f'Total de {n10} cédulas de R$ 10')
if n1 > 0:
    print(f'Total de {n1} moedas de R$ 1')
print('='*40)
print('VOLTE SEMPRE AO BANCO DEV!!!')
