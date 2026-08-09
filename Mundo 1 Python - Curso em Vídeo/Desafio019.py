from random import choice
a = str(input('Digite o nome de um(a) aluno(a): '))
b = str(input('Digite o nome de mais um(a): '))
c = str(input('Digite mais um(a): '))
d = str(input('Por fim, mais um(a): '))
lista = [a,b,c,d]
print('O aluno(a) escolhido(a) foi {}'.format(choice(lista)))