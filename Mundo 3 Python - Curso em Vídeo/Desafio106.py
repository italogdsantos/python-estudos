def PyHelp():
    from time import sleep
    while True:
        print(30 * '\033[4;97;46m~~')
        print(15*' ','SISTEMA DE AJUDA PYHELP')
        print(30 * '~~')
        sleep(0.5)
        bib = str(input('\033[mDigite o nome de uma biblioteca ou função->')).lower()
        sleep(0.5)
        if bib == 'fim':
            break
        print(30 * '\033[4;97;43m~~')
        print(10*' ', f"Acessando o manual do comando '{bib}'")
        print(30 * '~~')
        print('\033[m')
        sleep(0.5)
        print('\033[4;30;107m')
        help(bib)
        print('\033[m')
    print('Obrigado por usar o meu programa!')

PyHelp()