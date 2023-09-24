x = float(input('Quanto mede o 1º segmento de reta: '))
y = float(input('Quanto mede o 2º segmento de reta: '))
z = float(input('Quanto mede o 3º segmento de reta: '))

if (x + y) > z and (z + x) > y and (y + z) > x:
    print('Possível.')
else:
    print('Impossível.')
    