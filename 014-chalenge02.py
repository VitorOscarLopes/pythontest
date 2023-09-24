x = float(input('Digite um número: '))
y = float(input('Digite um número: '))
c = 0
while c != 5:
    print('-=-'*14)
    print('                  MENU')
    print('-=-'*14)
    print(' [1]Somar \n [2]Multiplicar \n [3]Maior \n [4]Escolher outros números \n [5]Encerrar')
    print('-=-' * 14)
    c = int(input('Escolha: '))
    if c == 1:
        print('A soma de {} mais {} é {}'.format(x, y, x + y))
    else:
        if c == 2:
            print('O produto de {} e {} é {}'.format(x, y, x * y))
        else:
            if c == 3:
                if x > y:
                    maior = x
                else:
                    if y > x:
                        maior = y
                if x == y:
                    print('Os dois valores digitados são iguais.')
                else:
                    print('O maior valor digitado foi {}'.format(maior))
            else:
                if c == 4:
                    x = float(input('Digite um número: '))
                    y = float(input('Digite um número: '))
