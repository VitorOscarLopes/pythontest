from time import sleep

x = int(input('Digite um número: '))
print('-=-' * 20)
print('ANALISANDO.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', '')
print('-=-' * 20)

div = -2
for c in range(1, x + 1):
    if x % c == 0:
        print('\033[31m', end='')
        div += 1
    else:
        print('\033[33m', end='')
    print(c, '\033[m', end=' ')
print()
if div == 0 or x == 1:
    print('Número {} é PRIMO!'.format(x))
else:
    print('O número {} NÃO é primo!'.format(x))
