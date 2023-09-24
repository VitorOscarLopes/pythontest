n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
s = 0
for c in range(n, n+r*10, r):
    print(c)
