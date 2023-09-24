from time import sleep


def lin():
    print('-=' * 25)


def contagem(x, y, z):
    lin()
    if z < 0:
        z *= -1
    print(f'Contagem de {x} até {y} de {z} em {z}')
    if x > y:
        for c in range(x, y - 1, z * (-1)):
            print(c, end=' ')
            sleep(0.3)
    for c in range(x, y + 1, z):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
lin()
print(' Agora é sua vez de personalizar a contagem!')
lin()
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
