import random

print('-=-' * 22)
print('                ESCOLHA UM NÚMERO DE 1 Á 10')
print('-=-' * 22)
user = int(input('Escolha um número de 0 à 10: '))
maq = random.randint(1, 10)
tent = 0
while maq != user:
    if user != maq:
        print('VOCÊ ERROU! Eu escolhi outro número. Tente novamente.')
        tent += 1
        user = int(input('Escolha um número de 0 à 10: '))
if user == maq:
    print('VOCÊ ACERTOU ', end='')
    tent += 1
if tent > 1:
    print('depois de {} tentativas.'.format(tent))
else:
    print('DE PRIMEIRA!')
