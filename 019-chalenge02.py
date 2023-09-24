import datetime
pessoa = dict()
pessoa['nome'] = str(input('Qual o seu nome? '))
pessoa['nascimento'] = int(input('Em que ano nasceu? '))
pessoa['ctps'] = int(input('Carteira de  trabaho(0 = NÃO TEM): '))
if pessoa['ctps'] != 0:
    pessoa['contrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Qual o salário? '))
    print(pessoa)
    print(f'O nome é {pessoa["nome"]}')
    print(f'A idade é {datetime.datetime.now().year - pessoa["nascimento"]}')
    print(f'O CTPS é {pessoa["ctps"]}')
    print(f'O salário tem o valor de {pessoa["salario"]} reais')
    print(f'Você pode se aposentar com {(datetime.datetime.now().year - pessoa["contrato"]) + 35 + (datetime.datetime.now().year - pessoa["nascimento"])} anos')
    print(f'Ano de contratação {pessoa["contrato"]}')
else:
    print('-='*20)
    print(pessoa)
    print(f'O nome é {pessoa["nome"]}')
    print(f'A idade é {datetime.datetime.now().year - pessoa["nascimento"]}')
    print(f'O CTPS é {pessoa["ctps"]}')
    