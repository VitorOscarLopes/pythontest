frase = str(input('Digite uma frase: ')).strip()

frase0: int = frase.lower().count('a')
frase1: int = frase.lower().find('a') + 1
frase2: int = frase.lower().rfind('a') + 1
print('A letra "a" aperece {} vezes.'.format(frase0))
print('A letra "a" aperece pela primeira vez na posição {}.'.format(frase1))
print('A letra "a" aperece pela ultima vez na posição {}.'.format(frase2))
