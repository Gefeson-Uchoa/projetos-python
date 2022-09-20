from modulos import  *
linha()
print(f'    Manipulando Arquivos')
linha()

while True:
    print('''[1] Mover.
[2] Copiar.
[3] Excluir
[4] Sair''')
    try:
        opcao =  int(input('Opçao: ')) # verifica se o usuario digitou uma opçao valida, cas0 contrario abri exeption
        if opcao == 4:
            break
    except:
        print('\033[1;31mescolha uma opçao valida\033[m')

    if opcao ==1:       # agora vamos tratar os arquivos de acordo com a opçao escolhida.
        especifico1= especifico()
        if especifico1 == 1:
            caminho = input('digite o caminho atual dos arquivos: ') # digitar caminho completo.
            caminho_novo = input('digite o caminho pra onde vai os arquivos: ')
            move(caminho,caminho_novo)
            print('\033[1;35mArquivos movidos com sucesso.\033[m')
        if especifico1 == 2:
            print('\033[1;36mdica, se desejar um arquivo especifico, cole o nome dele aqui, ou algum termimo, tipo '
                  '".pdf"\033[m')
            caminho = input('digite o caminho atual dos arquivos: ')  # digitar caminho completo.
            caminho_novo = input('digite o caminho pra onde vai os arquivos: ')
            termo = input('digite o arquivo ou termo: ')
            moveE(caminho, caminho_novo,termo)
            print('\033[1;35mArquivos movidos com sucesso.\033[m')
        try:
            continua = continuar()
            if continua == 2:
                break
        except:
            break

    if opcao == 2:
        especifico2 = especifico()
        if especifico2 == 1:
            caminho = input('digite o caminho atual dos arquivos: ')
            caminho_novo = input('digite o caminho pra onde vai os arquivos: ')
            copy(caminho,caminho_novo)
            print('\033[1;35mArquivos copiados com sucesso.\033[m')
        if especifico2 == 2:
            print('\033[1;36mdica, se desejar um arquivo especifico, cole o nome dele aqui, ou algum termimo, tipo '
                  '".pdf"\033[m')
            caminho = input('digite o caminho atual dos arquivos: ')
            caminho_novo = input('digite o caminho pra onde vai os arquivos: ')
            termo = input('digite o arquivo ou termo: ')
            copyE(caminho, caminho_novo,termo)
            print('\033[1;35mArquivos copiados com sucesso.\033[m')
        try:
            continua = continuar()
            if continua == 2:
                break
        except:
            break
    if opcao ==3:
        while True:
            especifico = especifico()
            if especifico ==1:
                caminho = input('digite o caminho da pasta: ')
                excluir(caminho)
                print('\033[1;35mArquivos excluidos.\033[m')
                break
            elif especifico ==2:
                print('\033[1;36mdica, se desejar um arquivo especifico, cole o nome dele aqui, ou algum termimo, tipo '
                      '".pdf"\033[m')
                caminho = input('digite o caminho da pasta: ')
                termo = input('digite o arquivo ou termo: ')
                excluirE(caminho,termo)
                print('\033[1;35mArquivos excluidos.\033[m')
                break
        try:
            continua = continuar()
            if continua >= 2:
                break
        except:
            break