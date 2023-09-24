tabela = ('Botafogo', 'Palmeiras', 'Gremio', 'Flamengo', 'Fluminense', 'Bragantino', 'Atlético Paranaense',
          'Fortaleza', 'Atlético Mineiro', 'Cuiaba', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás',
          'Bahia', 'Santos', 'Vasco da Gama', 'América', 'Coritiba')
esc = 0
while esc != 5:
    print('\033[0:36m='*40, f'\n{"BRASILEIRÃO":^40}\n'+'='*40)
    print('\033[m[1]Top 5 times.\n[2]Zona de rebaixamento.\n[3]Times em ordem alfabetica.\n[4]Em que posição da tabela '
          'está seu time.\n[5]Sair.\n'+'='*40)
    esc = int(input('Escolha: '))
    if esc == 1:
        for pos, time in enumerate(tabela[0:5]):
            print(f'{pos+1:>3}º - {time}')
    elif esc == 2:
        for pos in range(16, 20):
            print(f'{pos+1:>3}º - {tabela[pos]}')
    elif esc == 3:
        for pos in range(len(tabela)):
            print(f'{sorted(tabela)[pos]}')
    elif esc == 4:
        timepos = (input('Qual o nome do seu time: ')).title()
        timepos1 = tabela.index(timepos)
        print(f'{timepos}, está em {timepos1+1}º no Brasileirão.')
