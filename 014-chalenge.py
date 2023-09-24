c = 0
while c < 1:
    sexo = str(input('Qual seu sexo(M/F): ')).upper()
    if sexo == 'F':
        print('Fêmea')
        c += 1
    else:
        if sexo == 'M':
            print('Macho')
            c += 1
        else:
            print('Sexo inválido! Tente novamente')
