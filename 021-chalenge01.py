def fatorial(numero, show):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    if show is False:
        print(f)
    else:
        for c in range(numero, 1, -1):
            print(f'{c} x ', end='')
        print(f'1 = {f}')


fatorial(6, True)
