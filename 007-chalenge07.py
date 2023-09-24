x = float(input("Qual é a altura da parede: "))
y = float(input("Qual é a largura da parede: "))
a = x * y
t = a / 2
print('A quantidade de tinta necessária para pintar sua parede de {:.2f} m^2, em litros, é {:.3f}.'.format(a, t))
