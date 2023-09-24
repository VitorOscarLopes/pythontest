estado = dict()
brasil = list()
for c in range(0, 3):
    estado['Nome'] = str(input('Qual o nome do estado: '))
    estado['sigla'] = str(input('Qual o a sigla: '))
    brasil.append(estado.copy())

for estado in brasil:
    print(f'A sigla de {estado["Nome"]} é {estado["sigla"]}.')
