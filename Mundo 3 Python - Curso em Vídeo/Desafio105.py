def notas(*nota: float, sit=False):
    boletim = {}
    boletim['total'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['media'] = (sum(nota) / len(nota))
    if sit:
        if boletim['media'] <= 5:
            boletim['situação'] = "RUIM"
        if boletim['media'] > 5 and boletim['media'] < 7:
            boletim['situação'] = "RAZOÁVEL"
        if boletim['media'] >= 7 and boletim['media'] < 10:
            boletim['situação'] = "BOA"
        if boletim['media'] == 10:
            boletim['situação'] = "PERFEITA!"
    return boletim

n1 = notas(7, 5.5, 8, sit=True)
n2 = notas(10,10,10,  sit=True)
n3 = notas(1.5, 2, 4)
print(n1)
print(n2)
print(n3)