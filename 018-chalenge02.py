totpar = s3f = 0
maior = list()
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for d in range(0, 3):
        matriz[c][d] = (int(input(f'Digite um número [{c}, {d}]: ')))
        if matriz[c][d] % 2 == 0:
            totpar += matriz[c][d]
        if matriz[c][2]:
            s3f += matriz[c][2]
        if matriz[1][d]:
            maior.append(matriz[1][d])
for q in range(0, 3):
    for w in range(0, 3):
        print(f'[{matriz[q][w]:0>3}]', end='')
    print()
maior = sorted(maior)
print('-='*30)
print(f'A soma dos números pares é {totpar}')
print(f'A soma dos valores da terceira coluna é {s3f}')
print(f'O maior número na segunda linha é o {maior[-1]}')
