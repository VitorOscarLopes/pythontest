resp = 'S'
nums = list()
while resp != 'N':
    num = (int(input('Digite um número: ')))
    if num in nums:
        print('RESPOSTA INVALIDA! Número DUPLICADO!')
    elif num not in nums:
        nums.append(num)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar?[S/N] ')).upper()
    print('-=-'*20)
print(f'Você digitou {sorted(nums)}')
