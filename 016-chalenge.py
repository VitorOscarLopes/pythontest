num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
while True:
    esc = int(input('Digite um número: '))
    if esc > 20 or esc < 0:
        print('Tente novamente. ', end='')
    else:
        print(f'Vocè digitou o número {num[esc]}.')
        break
