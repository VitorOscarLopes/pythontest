from datetime import datetime


def voto(nascimento):
    idade = datetime.today().year - nascimento
    if idade < 18:
        return print(f'Com {idade} anos: VOTO NEGADO!')
    else:
        if 18 < idade < 65:
            return print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
        else:
            return print(f'Com {idade} anos: VOTO OPICIONAL!')


nasc = int(input('Ano de nascimento: '))
voto(nasc)
