x = int(input('Digite a idade do atleta: '))
if x <= 9:
    print('O atleta é classificado como MIRIM.')
elif x > 9 and x <= 14:
    print('O atleta é classificado como INFANTIL.')
elif x > 14 and x <= 19:
    print('O atleta é classificado como JUNIOR.')
elif x == 20:
    print('O atleta é classificado como SÊNIOR.')
elif x > 20:
    print('O atleta é classificado como MASTER.')