s = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
print('A soma de todos os números ímpares e multiplos de três de 1 à 500 é {}'.format(s))
