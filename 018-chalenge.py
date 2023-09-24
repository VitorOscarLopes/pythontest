grupo = list()
dado = list()
while True:
    dado.append((input('Nome: ')))
    dado.append((input('Peso: ')))
    grupo.append(dado[:])
    dado.clear()
    r = str(input('Deseja continuar? '))
    print('-=-'*20)
    if r == 'n':
        break
print(f'Ao total foram cadastradas {len(grupo)} pessoas.')
ordem = list()
for peso in grupo:
    ordem.append(peso[1])
maior = sorted(ordem)
print(f'O maior peso foi {ordem[-1]} com a(s) pessoa(s) ', end='')
for pessoa in grupo:
    if pessoa[1] in ordem[-1]:
        print(f'{pessoa[0]}...', end='')
print(f'\nO menor peso foi {ordem[0]} com a(s) pessoa(s) ', end='')
for pessoa in grupo:
    if pessoa[1] in ordem[0]:
        print(f'{pessoa[0]}...', end='')

