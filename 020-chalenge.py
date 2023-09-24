def area(a, b):
    ar = a * b
    print(f'A área do terreno mede: {ar:.2f}m²')


def lin():
    print('-'*30)


lin()
print('     CONTROLE DE TERRENO')
lin()
x = float(input('Qual a medida x do terreno(m)? '))
y = float(input('Qual a medida y do terreno(m)? '))
lin()
area(x, y)
