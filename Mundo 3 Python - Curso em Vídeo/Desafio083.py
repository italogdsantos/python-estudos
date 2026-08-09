lista = []
expressao = (str(input('Digite uma expressão: ')))
for n in expressao:
    if n == '(':
        lista.append('(')
    if n == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            pilha.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
