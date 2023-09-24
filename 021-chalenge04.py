def notas(*n, sit=False):
    dicio = dict()
    dicio['total'] = len(n)
    dicio['maior'] = sorted(n)[-1]
    dicio['menor'] = sorted(n)[0]
    dicio['media'] = sum(n) / len(n)
    if sit is True:
        if dicio['media'] >= 7:
            dicio['situacao'] = 'BOA'
        else:
            dicio['situacao'] = 'RUIM'
    return dicio


resp = notas(3, 10, 0, 6, sit=True)
print(resp)
