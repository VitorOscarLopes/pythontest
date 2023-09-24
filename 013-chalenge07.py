frase = str(input('Digite uma frase: ')).strip().lower()
x: str = frase.replace(' ', '')[::-1]      #frase sem espaço e invertida
y: str = frase.replace(' ', '')            #frase sem espaço
if x == y:
    print('É um palindromo')
else:
    print('Não é um palindromo')
