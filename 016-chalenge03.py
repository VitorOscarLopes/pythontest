n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais número: ')),
     int(input('Digite um ultimo número: ')))
print(f'Quantidade de 9 digitados: {n.count(9)} ')
print(f'O número 3 apareceu na {n.index(3)+1}º posição.')
par = 0
for num in n:
    if num % 2 == 0:
        par += 1
print(f'Total de números pares digitados: {par}')
