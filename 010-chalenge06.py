sal = float(input('Qual o sálario do funcionario: '))
if sal > 1250:
    print('O salário com aumento é: {:.2f}'.format(sal + sal * 0.1))
else:
    print('O salário com aumento é: {:.2f}'.format(sal + sal * 0.15))
