n = int(input('Digite um número: '))
a = len(str(n).strip())
b = int(a)
m = n // 1000 - n // 10000 * 10
c = n // 100 - n // 1000 * 10
d = n // 10 - n // 100 * 10
u = n - n // 10 * 10

print('Algarismos: {}.'.format(a))
print('Milhar: {}.'.format(m))
print('Centena: {}.'.format(c))
print('Dezena: {}.'.format(d))
print('Unidade: {}.'.format(u))
