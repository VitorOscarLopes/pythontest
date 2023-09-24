jogador = dict()
gols = list()
totg = 0
jogador['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input('Qual o número de partidas? '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na {c + 1}° partida? '))
    gols.append(gol)
    totg += gol
    jogador['totg'] = totg
    jogador['gols'] = gols
print(jogador)
print('-='*30)
print(f'O campo "nome" tem o valor {jogador["nome"]}')
print(f'O campo "gols" tem o valor {jogador["gols"]}')
print(f'O campo totg tem o valor {jogador["totg"]}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c + 1} fez {jogador["gols"][c]} ')
print(f'Foi um total de {jogador["totg"]} gols.')
