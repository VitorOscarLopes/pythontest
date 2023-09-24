valor = []
for pos in range(0, 5):
    valor.append(int(input(f'Digite um número na posição {pos}: ')))
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {sorted(valor)[-1]} na posição {valor.index(max(valor))}')
print(f"O menor valor digitado foi {sorted(valor)[0]} na posição {valor.index(min(valor))}")
