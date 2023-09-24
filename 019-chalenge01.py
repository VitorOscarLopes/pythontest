from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
valor = list()
print('Valores sorteados:')
for k, j in jogadores.items():
    print(f'    O {k} tirou {j} no dado!')
    sleep(1)
ranking = list(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
print('RANKING:')
for i, j in enumerate(ranking):
    print(f'    {i+1}º foi o {j[0]} com {j[1]} pontos')
    sleep(1)
