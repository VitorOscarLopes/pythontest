i = int(input('Inicio: '))

s = 0
for c in range(i, i+6):
    if c % 2 == 0:
        s += c
print(s)
