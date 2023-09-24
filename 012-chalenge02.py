import datetime
nasc = int(input('Em que ano você nasceu: '))
alist = datetime.datetime.today().year - nasc
if 18 > alist:
    print('Você ainda não precisa se alistar. Volte em {} ano(s).'.format(18-alist))
elif 18 == alist:
    print('Você deve se alistar esse ano.')
else:
    print('Você deveria ter se alistado há {} ano(s).'.format(alist-18))
