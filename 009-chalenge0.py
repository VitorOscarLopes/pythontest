nome = (str(input('Digite seu nome:'))).strip()
nomemiusc = nome.upper()
nomeminus= nome.lower()
nome1 = nome.split()
totnome = len(nome1)
totnome1 = len(nome1[0])
print('ANALISANDO NOME...')
print('=====================================================')
print('Seu nome em letras maiusculas:', nomemiusc)
print('Seu nome em letras minusculas:', nomeminus)
print('Quantidade de caracteres no nome:', len(nome) - nome.count(' '))
print('Seu primeiro nome:', nome1[0])
print('Quantidade de caractere no primeiro nome:', totnome1)
