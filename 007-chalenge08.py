x = float(input('Qual o valor do produto: '))
d = int(input('Qual o valor do desconto(%): '))
r = x - (x * (d / 100))

print('O valor final do produto é {:.2f} reais.'.format(r))
