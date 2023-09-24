nome = str(input('Qual o nome do Aluno: '))
nota1 = float(input('Qual a primeira nota de {}: '.format(nome)))
nota2 = float(input('Qual a segunda nota de {}: '.format(nome)))

m = (nota1 + nota2)/2

print('A média de {} vale {:.2f}.'.format(nome, m))
