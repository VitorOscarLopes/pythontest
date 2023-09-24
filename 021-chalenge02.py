def jogador(g='0', nome=''):
    if nome == '':
        print('O jogador <desconhecido> fez ', end='')
    else:
        print(f'O jogador {nome} fez ', end='')
    if g in '0':
        print('0 gol(s) no campeonato.')
    else:
        print(f'{g} gol(s) no campeonato.')


name = str(input('Nome do jogadagor: '))
gols = input('Quantidade de gol(s):')
jogador(gols, name)
