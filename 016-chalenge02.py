import random
nums = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
        random.randint(0, 10), random.randint(0, 10))
print(f'Os números sorteados foram: ', end='')
for n in nums:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi: {max(nums)}')
print(f'O maior número sorteado foi: {min(nums)}')
