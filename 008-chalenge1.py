import math
co = int(input('Quanto mede o cateto oposto: '))
ca = int(input('Quanto mede o cateto ajacente: '))

hip = math.hypot(ca, co)
print('A hipotenusa vale {}.'.format(hip))
