from datetime import date
cadastro = {}
ano_atual = date.today().year
while True:
    
    cadastro['nome'] = str(input('Digite o nome: '))
    cadastro['idade'] = int(input('Digite o ano de nascimento: ')
    if ano_atual - cadastro['idade'] < 16:
        print(f'Situação irregular, pela lei você não deveria trabalhar!')
        break

    cadastro['ano'] = int(input('Ano de contratação: '))

    if cadastro['ano'] - cadastro['idade'] < 16:
        print(f'Situação irregular, pela lei você não deveria contribuir com tal idade!')
        break

    cadastro['ctps'] = int(input('Digite a sua CTPS (0 se não tiver): '))

    if cadastro['ctps'] == 0:
        print(30*'-=')
        print(f' - O nome é: {cadastro["nome"]}')
        print(f' - {cadastro["nome"]} nasceu no ano: {cadastro["idade"]}')
        print(f' - {cadastro["nome"]} não tem CTPS')
        break

    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['ano'] + 35

    print(30*'=-')
    print(f'Nome: {cadastro["nome"]}')
    print(f'Idade: {ano_atual - cadastro["idade"]} anos')
    print(f'CTPS: {cadastro["ctps"]}')
    print(f'Contratação: {cadastro["ano"]}')
    print(f'Salário: R${cadastro["salário"]:.2f}')
    print(f'Aposenta em: {cadastro["aposentadoria"]} com {cadastro["aposentadoria"] - cadastro["idade"]} anos de idade.')
    print(30*'=-')
    break
