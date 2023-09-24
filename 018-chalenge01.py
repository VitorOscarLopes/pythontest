valor = list()
for c in range(0, 3):
    for d in range(0, 3):
        valor.append(int(input(f'Digite um número({c}, {d}):')))
for p in range(0, 9, 3):
    print(f'[{valor[p]:0>3}] [{valor[p+1]:0>3}] [{valor[p+2]:0>3}]')
