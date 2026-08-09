from datetime import date, time, datetime, timedelta
ano = datetime.today().year
x = int(input('Digite o seu ano de nascimento para o Alistamento Militar: '))
if ano - x == 2005:
    print('Você DEVE se alistar no Exército esse ano.')
elif ano - x > 2005:
    y = ano - x - 2005
    print('Você ainda não tem idade de se alistar no Exército, faltam anos {} para você se alistar.'.format(y))
elif ano - x < 2005:
    print('Já passou do seu tempo de se alistar no Exército, caso não tenha se alistado, procure se alistar imediatamanete!')