import random
print('-=-'*20)
print('{:^60}'.format('PAR OU ÍMPAR'))
print('-=-'*20)
win = 0
while True:
    player = int(input('Escolha um número: '))
    player1 = str(input('Par ou Ímpar: ')).upper()
    print('---' * 20)
    pc = random.randint(1, 10)
    if player1 == 'IMPAR':
        pc1 = 'PAR'
    else:
        pc1 = 'IMPAR'
    if (pc + player) % 2 == 0:
        paridade = 'PAR'
    else:
        paridade = 'IMPAR'
    print(f'O PC escolheu {pc1.title()} e o número {pc}.')
    print('---' * 20)
    print(pc, '+', player, '=', pc + player)
    print('---' * 20)
    print(f'{pc + player} é {paridade}')
    if pc1 == paridade:

        print('Você \033[4:31mPERDEU\033[m!')
        print('\033[4:33m-=-\033[m' * 20)
        break
    else:
        print('Você \033[4:34mGANHOU\033[m!')
        win += 1
        print('\033[4:33m-=-\033[m' * 20)
if win == 0:
    print('Você perdeu de primeira.')
else:
    if win == 1:
        print('Venceu apenas uma vez.')
    elif win > 1:
        print(f'Total de {win} vitórias seguidas!')
