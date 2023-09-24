from random import randint
from time import sleep
numeros = list()


def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
    for n in numeros:
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares {lista}, temos {s}')


sorteio(numeros)
somapar(numeros)
