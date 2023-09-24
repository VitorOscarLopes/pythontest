grupo = list()
pessoa = dict()
totp = toti = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo(M/F): '))
    pessoa['idade'] = int(input('Qual a idade: '))
    r = str(input('Deseja continuar?(S/N)'))
    totp += 1
    grupo.append(pessoa.copy())
    if r in 'Nn':
        print('-='*30)
        break
print(f'O grupo tem um total de {totp} pessoas.')
for p in grupo:
    toti += p['idade']
imed = toti / totp
print(f"A idade média do grupo é {imed}.")
print(f'As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'f':
        print(p['nome'], end='; ')
print('\nLista de pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > imed:
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')
