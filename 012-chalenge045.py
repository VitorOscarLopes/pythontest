from random import randint
print('-=-'*20)
print('                          JOKENPÔ')
print('-=-'*20)
print('[1]TESOURA')
print('[2]PEDRA')
print('[3]PAPEL')
print('-=-'*20)

esc = int(input())
maq = randint(1, 3)

print('-=-'*20)
if maq == 1:
    maqesc: str = 'Tesoura'
elif maq == 2:
    maqesc: str = 'Pedra'
elif maq == 3:
    maqesc: str = 'Papel'

if esc == maq:
    print('A máquina também escolheu {} e você \033[1;33mEMPATOU\033[m!'.format(maqesc))

if maq == 1 and esc == 3:
    print('A máquina escolheu Tesoura. Você \033[1;31mPERDEU\033[m!')
elif maq == 1 and esc == 2:
    print('A máquina escolheu Tesoura. Você \033[1;36mGANHOU\033[m!')

if maq == 2 and esc == 1:
    print('A máquina escolheu Pedra. Você \033[1;31mPERDEU\033[m!')
elif maq == 2 and esc == 3:
    print('A máquina escolheu Pedra. Você \033[1;36mGANHOU\033[m!')

if maq == 3 and esc == 2:
    print('A máquina escolheu Papel. Você \033[1;31mPERDEU\033[m!')
elif maq == 3 and esc == 1:
    print('A máquina escolheu Papel. Você \033[1;36mGANHOU\033[m!')
