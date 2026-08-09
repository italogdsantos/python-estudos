print(38*'-')
print(8*' ','LOJA SUPER BARATÃO')
print(38*'-')
preco = total = barato = contmil = cont  = 0
produto_b = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    print(38 * '-')
    total += preco
    cont += 1
    if cont == 1:
        barato = preco
        produto_b = produto
    else:
        if preco < barato:
            barato = preco
            produto_b = produto
    if preco > 1000:
        contmil += 1
    if continuar in 'N':
        break
print(f'A compra total deu R${total:.2f}.')
print(f'Temos {contmil} produtos acima de R$1000.00.')
print(f'O produto mais barato foi {produto_b} e custa R${barato:.2f}.')