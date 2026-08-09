mv = int()
mi =  float()
nv = str()
tm = int()

for c in range (1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome:'))
    idade = float(input('Idade:'))
    mi += idade
    sexo = str(input('Sexo (F/M):')).strip()

    if sexo == 'M' and idade > mv:
        mv = 0
        mv += idade
        nv =''
        nv += nome

    if sexo == 'F' and idade < 20:
        tm += 1

print('A media de idade do grupo é de {} anos'.format(mi/4))
print('O homem mais velho tem {:.0f} anos e se chama {}'.format(mv,nv))
print('Ao todo são {} mulheres com menos de 20 anos'. format(tm))
