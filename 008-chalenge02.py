import random

a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do quarto aluno: '))
lista = [a4, a3, a2, a1]
sort = random.choice(lista)
print('O aluno aluno escolhido foi:', sort+'.')
