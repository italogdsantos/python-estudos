import random
a = str(input('Digite o nome do aluno para o sorteio '))
b = str(input('Digite mais um nome '))
c = str(input('Digite mais um '))
d = str(input('Digite mais um '))
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem de apresentação será' '\n',(lista))