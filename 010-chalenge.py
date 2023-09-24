import random
n = int(input('Escolha um número de 1 à 5: '))
n1 = random.choice([1, 2, 3, 4, 5])

if n1 == n:
    print('Você e a máquina escolheram o mesmo número.({})'.format(n1))
else:
    print('Você escolheu um número diferente do da máquina.({}, {})'.format(n, n1))
