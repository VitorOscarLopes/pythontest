aluno = dict()
aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['media'] = int(input(f'Qual a média de {aluno["nome"]}?'))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do aluno é {aluno["media"]}')
if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
print(f'A situação de {aluno["nome"]} é {aluno["situacao"]}')
print(aluno)
