item = 'Lapis', 3.00, 'Caneta', 2.50, 'Estojo', 12.50, 'Caderno', 15.75, 'Borracha', 2.00
tabela = 0
while tabela < 10:
    print(f'{item[tabela]:.<25} R$ {item[tabela+1]:5.2f}')
    tabela += 2
